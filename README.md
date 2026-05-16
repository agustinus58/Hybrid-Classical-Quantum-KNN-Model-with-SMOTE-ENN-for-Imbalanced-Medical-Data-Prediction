# Hybrid Classical–Quantum KNN Model with SMOTE-ENN for Imbalanced Medical Data Prediction
This repository contains implementations and experiments of Classical k-Nearest Neighbor (k-NN) and Quantum k-Nearest Neighbor (QKNN) based on the SWAP test for medical data classification. This study proposes an integrated data processing pipeline that combines Principal Component Analysis (PCA), SMOTE-ENN, and multi-distance analysis, and is evaluated using K-Fold Cross-Validation

## Prasyarat
- It is recommended to use Anaconda Python 3.8.10
- with the following main libraries:
  ```shell
  pennylane, numpy, pandas, scikit-learn, imbalanced-learn, matplotlib, seaborn, shap
  ```
- It is recommended to create *virtual environment*:
```shell
  conda create "venv" -n qknn python=3.8.10
  conda activate qknn
```
This study was conducted on a computer equipped with an Intel Core i7 processor and 8 GB of RAM. To use PennyLane in Google Colab, it is necessary to configure the Python environment within the Colab notebook, followed by the installation of the required packages. *PennyLane, NumPy, and Matplotlib*. In this study, the quantum simulator provided by *PennyLane*, specifically *default.qubit*. 
