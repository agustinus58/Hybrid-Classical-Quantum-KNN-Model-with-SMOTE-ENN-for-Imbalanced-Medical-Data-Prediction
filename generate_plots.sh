#!/bin/bash
# ============================================================
# Generate Plots Script
# ============================================================
# This script generates all figures used in the paper:
# - Accuracy, Precision, Recall, F1-score
# - Before vs After SMOTE-ENN
# - KNN vs QKNN comparison
#
# Output figures are saved in results/figures/
# ============================================================

echo "============================================"
echo " Generating Plots for QKNN vs KNN Experiments"
echo "============================================"

PYTHON=python

# -----------------------------
# Directories
# -----------------------------
RESULTS_DIR="results"
FIGURES_DIR="results/figures"

mkdir -p ${FIGURES_DIR}

# -----------------------------
# Plot Configuration
# -----------------------------
DATASETS=(
  pima
  liver
  obesity
  breast_cancer
)

METRICS=(
  accuracy
  precision
  recall
  f1_score
)

MODELS=(
  knn
  qknn
)

# -----------------------------
# Generate Heatmaps
# -----------------------------
echo "[INFO] Generating heatmaps..."

for DATASET in "${DATASETS[@]}"; do
  for METRIC in "${METRICS[@]}"; do

    ${PYTHON} src/plot_heatmap.py \
      --results_dir ${RESULTS_DIR} \
      --dataset ${DATASET} \
      --metric ${METRIC} \
      --output ${FIGURES_DIR}/heatmap_${DATASET}_${METRIC}.png

  done
done

# -----------------------------
# Generate Model Comparison Plots
# -----------------------------
echo "[INFO] Generating KNN vs QKNN comparison plots..."

for DATASET in "${DATASETS[@]}"; do
  for METRIC in "${METRICS[@]}"; do

    ${PYTHON} src/plot_comparison.py \
      --results_dir ${RESULTS_DIR} \
      --dataset ${DATASET} \
      --metric ${METRIC} \
      --output ${FIGURES_DIR}/compare_${DATASET}_${METRIC}.png

  done
done

# -----------------------------
# Generate Before vs After SMOTE-ENN Plots
# -----------------------------
echo "[INFO] Generating before vs after SMOTE-ENN plots..."

for DATASET in "${DATASETS[@]}"; do
  for METRIC in "${METRICS[@]}"; do

    ${PYTHON} src/plot_balancing_effect.py \
      --results_dir ${RESULTS_DIR} \
      --dataset ${DATASET} \
      --metric ${METRIC} \
      --output ${FIGURES_DIR}/balancing_${DATASET}_${METRIC}.png

  done
done

echo "============================================"
echo " All plots generated successfully!"
echo " Figures saved in '${FIGURES_DIR}' "
echo "============================================"
