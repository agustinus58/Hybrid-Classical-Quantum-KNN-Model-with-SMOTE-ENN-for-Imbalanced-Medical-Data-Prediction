#!/bin/bash
# ============================================================
# Quantum k-NN (QKNN) vs Classical k-NN
# Experiment Runner Script
# ============================================================
# Pipeline:
# Dataset → PCA → SMOTE-ENN → KNN / QKNN (SWAP-Test)
# → Multi-Distance → K-Fold Cross Validation
#
# NOTE:
# - This script may take a long time to execute
# - Recommended to run on a machine with sufficient resources
# ============================================================

echo "============================================"
echo " Starting QKNN vs KNN Experiments "
echo "============================================"

# -----------------------------
# Global Configuration
# -----------------------------
PYTHON=python
SEED=42
FOLDS=5
K_VALUES=(3 5 7)

DISTANCES=(
  euclidean
  manhattan
  canberra
  chebyshev
  chi-square
  mahalanobis
  polar
)

DATASETS=(
  pima
  liver
  obesity
  breast_cancer
)

# -----------------------------
# Output Directories
# -----------------------------
RESULTS_DIR="results"
LOG_DIR="logs"

mkdir -p ${RESULTS_DIR}
mkdir -p ${LOG_DIR}

# -----------------------------
# Run Experiments
# -----------------------------
for DATASET in "${DATASETS[@]}"; do
  echo "--------------------------------------------"
  echo " Dataset: ${DATASET}"
  echo "--------------------------------------------"

  for K in "${K_VALUES[@]}"; do
    for DIST in "${DISTANCES[@]}"; do

      echo "Running:"
      echo "  Dataset   : ${DATASET}"
      echo "  k         : ${K}"
      echo "  Distance  : ${DIST}"

      # ============================
      # Classical k-NN
      # ============================
      ${PYTHON} src/run_knn.py \
        --dataset ${DATASET} \
        --k ${K} \
        --distance ${DIST} \
        --folds ${FOLDS} \
        --seed ${SEED} \
        --use_smoteenn \
        --use_pca \
        --output ${RESULTS_DIR}/knn_${DATASET}_k${K}_${DIST}.json \
        > ${LOG_DIR}/knn_${DATASET}_k${K}_${DIST}.log 2>&1

      # ============================
      # Quantum k-NN (SWAP-Test)
      # ============================
      ${PYTHON} src/run_qknn.py \
        --dataset ${DATASET} \
        --k ${K} \
        --distance ${DIST} \
        --folds ${FOLDS} \
        --seed ${SEED} \
        --use_smoteenn \
        --use_pca \
        --quantum_backend simulator \
        --output ${RESULTS_DIR}/qknn_${DATASET}_k${K}_${DIST}.json \
        > ${LOG_DIR}/qknn_${DATASET}_k${K}_${DIST}.log 2>&1

    done
  done
done

echo "============================================"
echo " All experiments completed successfully "
echo " Results saved in '${RESULTS_DIR}' "
echo " Logs saved in '${LOG_DIR}' "
echo "============================================"
