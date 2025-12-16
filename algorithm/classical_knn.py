# ============================================================
# Classical k-Nearest Neighbor (k-NN)
# ============================================================
# - Supports multiple distance metrics
# - Stratified K-Fold Cross-Validation
# - Returns fold-wise predictions for evaluation
# ============================================================

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold


# ------------------------------------------------------------
# Distance Metric Mapping
# ------------------------------------------------------------
def get_metric(metric_name):
    """
    Map metric name to scikit-learn compatible metric.
    """
    metric_map = {
        "euclidean": "euclidean",
        "manhattan": "manhattan",
        "canberra": "canberra",
        "chebyshev": "chebyshev",
        "chi-square": "chi2",
        "mahalanobis": "mahalanobis",
    }

    if metric_name not in metric_map:
        raise ValueError(f"Unsupported distance metric: {metric_name}")

    return metric_map[metric_name]


# ------------------------------------------------------------
# Classical KNN with Cross-Validation
# ------------------------------------------------------------
def run_classical_knn(
    X,
    y,
    k=3,
    distance="euclidean",
    n_folds=5,
    random_state=42
):
    """
    Run Classical k-NN using Stratified K-Fold CV.

    Parameters
    ----------
    X : np.ndarray
        Feature matrix (after preprocessing)
    y : np.ndarray
        Label vector
    k : int
        Number of nearest neighbors
    distance : str
        Distance metric
    n_folds : int
        Number of CV folds
    random_state : int
        Random seed

    Returns
    -------
    fold_results : list of dict
        Fold-wise true and predicted labels
    """

    metric = get_metric(distance)

    skf = StratifiedKFold(
        n_splits=n_folds,
        shuffle=True,
        random_state=random_state
    )

    fold_results = []

    for fold_idx, (train_idx, test_idx) in enumerate(skf.split(X, y), start=1):

        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        # ----------------------------------------------------
        # Mahalanobis requires covariance matrix
        # ----------------------------------------------------
        if metric == "mahalanobis":
            cov = np.cov(X_train, rowvar=False)
            VI = np.linalg.pinv(cov)

            knn = KNeighborsClassifier(
                n_neighbors=k,
                metric=metric,
                metric_params={"VI": VI}
            )
        else:
            knn = KNeighborsClassifier(
                n_neighbors=k,
                metric=metric
            )

        # Train
        knn.fit(X_train, y_train)

        # Predict
        y_pred = knn.predict(X_test)

        fold_results.append({
            "fold": fold_idx,
            "y_true": y_test.tolist(),
            "y_pred": y_pred.tolist()
        })

    return fold_results
