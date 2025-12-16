# SHAP Analysis Results

This folder contains the results of SHAP-based interpretability analysis
for the Classical k-Nearest Neighbor (k-NN) and Quantum k-Nearest Neighbor (QKNN)
models across all medical datasets used in this study.

## Folder Structure
- **Pima/**: Pima Indian Diabetes dataset
- **Liver/**: Liver Disease dataset
- **Obesity/**: Obesity dataset
- **BreastCancer/**: Breast Cancer dataset

## Visualization Types
- `*_shap_summary.png`  
  SHAP summary (beeswarm) plots illustrating the distribution of feature contributions.
- `*_shap_bar.png`  
  SHAP bar plots representing global feature importance.

## Notes
SHAP analysis is employed to compare the stability and consistency of feature contributions
between the classical k-NN and the SWAP-Test–based QKNN models,
both before and after class balancing using SMOTE-ENN.

These visualizations support the interpretability analysis presented
in Section 4 (Results and Discussion) of the main manuscript.
