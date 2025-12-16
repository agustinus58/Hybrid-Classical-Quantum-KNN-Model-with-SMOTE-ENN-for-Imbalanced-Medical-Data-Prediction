# ============================================================
# Quantum k-Nearest Neighbor (QKNN) - SWAP-Test
# ============================================================
# - Quantum feature encoding (Angle Embedding)
# - Similarity estimation via SWAP-Test (fidelity)
# - Polar distance (quantum-native)
# - Stratified K-Fold Cross-Validation
# ============================================================

import numpy as np
import pennylane as qml
from sklearn.model_selection import StratifiedKFold
from collections import Counter


# ------------------------------------------------------------
# Quantum Device Factory
# ------------------------------------------------------------
def create_swaptest_device(n_features, backend="simulator"):
    """
    Create a PennyLane device for SWAP-Test.
    Wires:
      0              : ancilla
      1..d           : |psi> (test sample)
      d+1..2d        : |phi> (training sample)
    """
    n_wires = 1 + 2 * n_features

    # Currently using simulator; hardware can be added later
    return qml.device("default.qubit", wires=n_wires, shots=None)


# ------------------------------------------------------------
# Quantum Feature Encoding
# ------------------------------------------------------------
def angle_embedding(x, wires):
    """
    Encode classical features using RY angle embedding.
    """
    for i, val in enumerate(x):
        qml.RY(val, wires=wires[i])


# ------------------------------------------------------------
# SWAP-Test Fidelity Estimation
# ------------------------------------------------------------
def swaptest_fidelity(x1, x2, dev):
    """
    Estimate fidelity F(|psi(x1)>, |psi(x2)>) using SWAP-Test.
    """

    d = len(x1)
    anc = 0
    wires_psi = list(range(1, d + 1))
    wires_phi = list(range(d + 1, 2 * d + 1))

    @qml.qnode(dev)
    def circuit():
        # Prepare ancilla
        qml.Hadamard(wires=anc)

        # Encode both states
        angle_embedding(x1, wires_psi)
        angle_embedding(x2, wires_phi)

        # Controlled-SWAP
        for i in range(d):
            qml.CSWAP(wires=[anc, wires_psi[i], wires_phi[i]])

        # Final Hadamard
        qml.Hadamard(wires=anc)

        # Measure ancilla
        return qml.expval(qml.PauliZ(anc))

    # Fidelity from SWAP-Test
    expval = circuit()
    fidelity = (1.0 + expval) / 2.0

    return np.clip(fidelity, 0.0, 1.0)


# ------------------------------------------------------------
# Polar Distance (Quantum-Native)
# ------------------------------------------------------------
def polar_distance(fid):
    """
    Polar distance derived from fidelity.
    d = arccos(sqrt(F))
    """
    return np.arccos(np.sqrt(fid))


# ------------------------------------------------------------
# Single-Sample QKNN Prediction
# ------------------------------------------------------------
def qknn_predict_single(x_test, X_train, y_train, k, dev):
    """
    Predict label for a single test sample using QKNN.
    """

    distances = []

    for x_tr, y_tr in zip(X_train, y_train):
        fid = swaptest_fidelity(x_test, x_tr, dev)
        dist = polar_distance(fid)
        distances.append((dist, y_tr))

    # Sort by distance
    distances.sort(key=lambda x: x[0])

    # Majority vote
    k_labels = [lbl for _, lbl in distances[:k]]
    return Counter(k_labels).most_common(1)[0][0]


# ------------------------------------------------------------
# QKNN with Stratified K-Fold CV
# ------------------------------------------------------------
def run_qknn(
    X,
    y,
    k=3,
    n_folds=5,
    backend="simulator",
    random_state=42
):
    """
    Run Quantum k-NN (SWAP-Test) with Stratified K-Fold CV.

    Parameters
    ----------
    X : np.ndarray
        Feature matrix (after preprocessing)
    y : np.ndarray
        Label vector
    k : int
        Number of nearest neighbors
    n_folds : int
        Number of CV folds
    backend : str
        Quantum backend (currently simulator)
    random_state : int
        Random seed

    Returns
    -------
    fold_results : list of dict
        Fold-wise true and predicted labels
    """

    n_features = X.shape[1]
    dev = create_swaptest_device(n_features, backend)

    skf = StratifiedKFold(
        n_splits=n_folds,
        shuffle=True,
        random_state=random_state
    )

    fold_results = []

    for fold_idx, (train_idx, test_idx) in enumerate(skf.split(X, y), start=1):

        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        y_true, y_pred = [], []

        for xt, yt in zip(X_test, y_test):
            pred = qknn_predict_single(
                xt,
                X_train,
                y_train,
                k=k,
                dev=dev
            )
            y_true.append(yt)
            y_pred.append(pred)

        fold_results.append({
            "fold": fold_idx,
            "y_true": y_true,
            "y_pred": y_pred
        })

    return fold_results
