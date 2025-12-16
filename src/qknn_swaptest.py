# ============================================================
# Quantum k-Nearest Neighbor (QKNN) with SWAP-Test
# ============================================================
# - Quantum feature encoding via Angle Embedding
# - Similarity estimation via SWAP-Test (fidelity)
# - Polar distance: d = arccos(sqrt(fidelity))
# ============================================================

import numpy as np
import pennylane as qml
from sklearn.model_selection import StratifiedKFold
from collections import Counter


# ------------------------------------------------------------
# Quantum Configuration
# ------------------------------------------------------------
def create_swaptest_device(n_features):
    """
    Creates a PennyLane device for SWAP-Test.
    Wires:
    0           : ancilla
    1..n        : |psi> (test sample)
    n+1..2n     : |phi> (training sample)
    """
    n_wires = 1 + 2 * n_features
    return qml.device("default.qubit", wires=n_wires, shots=None)


# ------------------------------------------------------------
# Quantum Feature Encoding
# ------------------------------------------------------------
def angle_embedding(x, wires):
    """
    Angle embedding using RY rotations.
    """
    for i, val in enumerate(x):
        qml.RY(val, wires=wires[i])


# ------------------------------------------------------------
# SWAP-Test Circuit
# ------------------------------------------------------------
def swap_test_circuit(x1, x2, dev):
    """
    Computes fidelity between x1 and x2 using SWAP-Test.
    """

    n_features = len(x1)
    ancilla = 0
    wires_psi = list(range(1, n_features + 1))
    wires_phi = list(range(n_features + 1, 2 * n_features + 1))

    @qml.qnode(dev)
    def circuit():
        # Prepare ancilla
        qml.Hadamard(wires=ancilla)

        # Encode states
        angle_embedding(x1, wires_psi)
        angle_embedding(x2, wires_phi)

        # Controlled SWAP
        for i in range(n_features):
            qml.CSWAP(wires=[ancilla, wires_psi[i], wires_phi[i]])

        # Final Hadamard
        qml.Hadamard(wires=ancilla)

        # Measure ancilla
        return qml.expval(qml.PauliZ(ancilla))

    # SWAP-Test relation:
    # fidelity = (1 + <Z>) / 2
    expval = circuit()
    fidelity = (1.0 + expval) / 2.0

    return fidelity


# ------------------------------------------------------------
# Polar Distance (Quantum-Native)
# ------------------------------------------------------------
def polar_distance_from_fidelity(fid):
    """
    Polar distance based on fidelity.
    d = arccos(sqrt(fid))
    """
    fid = np.clip(fid, 0.0, 1.0)
    return np.arccos(np.sqrt(fid))


# ------------------------------------------------------------
# QKNN Core
# ------------------------------------------------------------
def qknn_predict_single(x_test, X_train, y_train, k, dev):
    """
    Predict label for a single test sample using QKNN.
    """
    distances = []

    for x_tr, y_tr in zip(X_train, y_train):
        fid = swap_test_circuit(x_test, x_tr, dev)
        dist = polar_distance_from_fidelity(fid)
        distances.append((dist, y_tr))

    # Sort by distance
    distances.sort(key=lambda x: x[0])

    # k nearest neighbors
    k_nearest = distances[:k]
    labels = [lbl for _, lbl in k_nearest]

    # Majority vote
    most_common = Counter(labels).most_common(1)[0][0]
    return most_common


# ------------------------------------------------------------
# Cross-Validation Wrapper
# ------------------------------------------------------------
def run_quantum_knn(
    X,
    y,
    k=3,
    distance="polar",
    n_folds=5,
    backend="simulator",
    random_state=42
):
    """
    Run QKNN with SWAP-Test using Stratified K-Fold CV.
    """

    if distance != "polar":
        raise ValueError(
            "QKNN (SWAP-Test) currently supports only 'polar' distance"
        )

    n_features = X.shape[1]
    dev = create_swaptest_device(n_features)

    skf = StratifiedKFold(
        n_splits=n_folds,
        shuffle=True,
        random_state=random_state
    )

    fold_results = []

    for fold_idx, (train_idx, test_idx) in enumerate(skf.split(X, y), 1):
        y_true = []
        y_pred = []

        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

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
