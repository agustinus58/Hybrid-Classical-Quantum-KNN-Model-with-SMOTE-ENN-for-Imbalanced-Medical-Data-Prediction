#!/usr/bin/env python3
# ============================================================
# CLI Main Entry for KNN & QKNN Experiments
# ============================================================
# Pipeline:
# Dataset → Normalization → PCA → SMOTE-ENN
# → KNN / QKNN (SWAP-Test)
# → Multi-Distance → K-Fold Cross Validation
# ============================================================

import argparse
import json
import numpy as np
from pathlib import Path

from src.preprocessing import load_dataset, preprocess_data
from src.knn_classical import run_classical_knn
from src.qknn_swaptest import run_quantum_knn
from src.evaluation import evaluate_results


# ------------------------------------------------------------
# Argument Parser
# ------------------------------------------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="CLI for Classical KNN and Quantum KNN (SWAP-Test)"
    )

    parser.add_argument("--dataset", type=str, required=True,
                        choices=["pima", "liver", "obesity", "breast_cancer"],
                        help="Dataset name")

    parser.add_argument("--model", type=str, required=True,
                        choices=["knn", "qknn"],
                        help="Model type")

    parser.add_argument("--k", type=int, default=3,
                        help="Number of nearest neighbors")

    parser.add_argument("--distance", type=str, required=True,
                        choices=[
                            "euclidean",
                            "manhattan",
                            "canberra",
                            "chebyshev",
                            "chi-square",
                            "mahalanobis",
                            "polar"
                        ],
                        help="Distance metric")

    parser.add_argument("--folds", type=int, default=5,
                        help="Number of CV folds")

    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed")

    parser.add_argument("--use_pca", action="store_true",
                        help="Apply PCA")

    parser.add_argument("--use_smoteenn", action="store_true",
                        help="Apply SMOTE-ENN")

    parser.add_argument("--quantum_backend", type=str, default="simulator",
                        choices=["simulator", "ibmq"],
                        help="Quantum backend")

    parser.add_argument("--output", type=str, required=True,
                        help="Output JSON file")

    return parser.parse_args()


# ------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------
def main():
    args = parse_arguments()
    np.random.seed(args.seed)

    print("============================================")
    print(" Running Experiment ")
    print("============================================")
    print(f"Dataset  : {args.dataset}")
    print(f"Model    : {args.model}")
    print(f"k        : {args.k}")
    print(f"Distance : {args.distance}")
    print(f"Folds    : {args.folds}")
    print(f"PCA      : {args.use_pca}")
    print(f"SMOTE-ENN: {args.use_smoteenn}")
    print("============================================")

    # -----------------------------
    # Load Dataset
    # -----------------------------
    X, y = load_dataset(args.dataset)

    # -----------------------------
    # Preprocessing
    # -----------------------------
    X_proc, y_proc = preprocess_data(
        X, y,
        use_pca=args.use_pca,
        use_smoteenn=args.use_smoteenn,
        random_state=args.seed
    )

    # -----------------------------
    # Run Model
    # -----------------------------
    if args.model == "knn":
        fold_results = run_classical_knn(
            X_proc, y_proc,
            k=args.k,
            distance=args.distance,
            n_folds=args.folds,
            random_state=args.seed
        )

    elif args.model == "qknn":
        fold_results = run_quantum_knn(
            X_proc, y_proc,
            k=args.k,
            distance=args.distance,
            n_folds=args.folds,
            backend=args.quantum_backend,
            random_state=args.seed
        )

    else:
        raise ValueError("Unknown model type")

    # -----------------------------
    # Evaluation
    # -----------------------------
    metrics = evaluate_results(fold_results)

    # -----------------------------
    # Save Results
    # -----------------------------
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    result_json = {
        "dataset": args.dataset,
        "model": args.model,
        "k": args.k,
        "distance": args.distance,
        "folds": args.folds,
        "use_pca": args.use_pca,
        "use_smoteenn": args.use_smoteenn,
        "metrics": metrics,
        "fold_results": fold_results
    }

    with open(output_path, "w") as f:
        json.dump(result_json, f, indent=4)

    print(f"[INFO] Results saved to: {output_path}")
    print("============================================")


if __name__ == "__main__":
    main()
