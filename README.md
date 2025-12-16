# Quantum k-Nearest Neighbor (QKNN) berbasis SWAP-Test untuk Klasifikasi Data Medis
Repositori ini berisi implementasi dan eksperimen Classical k-Nearest Neighbor (k-NN) dan Quantum k-Nearest Neighbor (QKNN) berbasis SWAP-Test untuk klasifikasi data medis. Penelitian ini mengusulkan pipeline pemrosesan data terintegrasi yang mengombinasikan Principal Component Analysis (PCA), SMOTE-ENN, serta analisis multi-distance, dan dievaluasi menggunakan K-Fold Cross-Validation.

## Prasyarat
- Disarankan menggunakan Anaconda Python 3.8.10 
  dengan Library utama:
  ```shell
  pennylane, numpy, pandas, scikit-learn, imbalanced-learn, matplotlib, seaborn, shap
  ```
- Disarankan membuat *virtual environment*:
```shell
  conda create "venv" -n qknn python=3.8.10
  conda activate qknn
```
Penelitian ini dijalankan pada komputer dengan prosesor Intel Core i7 dan 8 GB RAM. Untuk menggunakan PennyLane di Google Colab, diperlukan pengaturan lingkungan Python di dalam notebook Colab, diikuti dengan instalasi *PennyLane, NumPy, dan Matplotlib*. Dalam penelitian ini digunakan simulator kuantum yang disediakan oleh *PennyLane*, yaitu *default.qubit*. 
