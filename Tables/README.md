# Experimental Results Tables

This directory contains the summarized experimental results of the study
"Quantum k-Nearest Neighbor (QKNN) with SWAP-Test for Medical Data Classification".

## Table Description
- Table S1: Pima Indian Diabetes
- Table S2: Liver Disease
- Table S3: Obesity
- Table S4: Breast Cancer

Each table reports the best-performing results in terms of:
Accuracy, Precision, Recall, and F1-score.

Detailed fold-wise results and full configurations are provided
in JSON format under the results/ directory.

# Table S1. Performance Comparison on Pima Indian Diabetes Dataset

This table reports Accuracy (Acc), Precision (Prec), Recall (Rec), and F1-score (F1)
for Classical k-NN (KNN) and Quantum k-NN (QKNN) across k = 3, 5, 7.
Results are shown for the imbalanced data and after SMOTE-ENN.

---

## A. Before Balancing (Imbalanced Data)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.83 | 0.87 | **0.87** | **0.87** |
| Euclidean | 5 | 0.83 | 0.87 | **0.88** | **0.87** |
| Euclidean | 7 | 0.84 | 0.86 | **0.90** | **0.88** |
| Manhattan | 3 | 0.83 | 0.86 | **0.88** | **0.87** |
| Manhattan | 5 | 0.84 | 0.87 | **0.89** | **0.88** |
| Manhattan | 7 | 0.85 | 0.87 | **0.91** | **0.89** |
| Canberra | 3 | 0.82 | 0.85 | **0.89** | **0.87** |
| Canberra | 5 | 0.83 | 0.86 | **0.89** | **0.87** |
| Canberra | 7 | 0.83 | 0.85 | **0.90** | **0.87** |
| Chebyshev | 3 | 0.81 | 0.86 | **0.86** | **0.86** |
| Chebyshev | 5 | 0.84 | 0.87 | **0.89** | **0.88** |
| Chebyshev | 7 | 0.84 | 0.86 | **0.90** | **0.88** |
| Chi-square | 3 | 0.52 | 0.63 | **0.68** | **0.65** |
| Chi-square | 5 | 0.53 | 0.63 | **0.73** | **0.68** |
| Chi-square | 7 | 0.87 | 0.90 | **0.92** | **0.91** |
| Mahalanobis | 3 | 0.83 | 0.86 | **0.89** | **0.88** |
| Mahalanobis | 5 | 0.84 | 0.87 | **0.90** | **0.88** |
| Mahalanobis | 7 | 0.84 | 0.86 | **0.91** | **0.88** |
| Polar Distance | 3 | 0.84 | 0.88 | **0.87** | **0.88** |
| Polar Distance | 5 | 0.85 | 0.88 | **0.89** | **0.89** |
| Polar Distance | 7 | 0.85 | 0.89 | **0.88** | **0.89** |

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.83 | 0.87 | **0.87** | **0.87** |
| Euclidean | 5 | 0.83 | 0.87 | **0.88** | **0.87** |
| Euclidean | 7 | 0.83 | 0.86 | **0.90** | **0.88** |
| Manhattan | 3 | 0.83 | 0.87 | **0.88** | **0.88** |
| Manhattan | 5 | 0.84 | 0.87 | **0.89** | **0.88** |
| Manhattan | 7 | 0.85 | 0.87 | **0.91** | **0.89** |
| Canberra | 3 | 0.82 | 0.85 | **0.88** | **0.86** |
| Canberra | 5 | 0.84 | 0.88 | **0.89** | **0.89** |
| Canberra | 7 | 0.84 | 0.87 | **0.90** | **0.88** |
| Chebyshev | 3 | 0.82 | 0.86 | **0.87** | **0.87** |
| Chebyshev | 5 | 0.83 | 0.87 | **0.89** | **0.88** |
| Chebyshev | 7 | 0.84 | 0.87 | **0.90** | **0.88** |
| Chi-square | 3 | 0.52 | 0.63 | **0.68** | **0.65** |
| Chi-square | 5 | 0.53 | 0.63 | **0.73** | **0.68** |
| Chi-square | 7 | 0.55 | 0.64 | **0.76** | **0.69** |
| Mahalanobis | 3 | 0.83 | 0.86 | **0.89** | **0.87** |
| Mahalanobis | 5 | 0.83 | 0.87 | **0.89** | **0.88** |
| Mahalanobis | 7 | 0.85 | 0.87 | **0.91** | **0.89** |
| Polar Distance | 3 | 0.83 | 0.88 | **0.88** | **0.88** |
| Polar Distance | 5 | 0.84 | 0.88 | **0.89** | **0.89** |
| Polar Distance | 7 | 0.84 | 0.87 | **0.89** | **0.88** |

---

## B. After Balancing (SMOTE-ENN)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.98 | 1.00 | **0.97** | **0.98** |
| Euclidean | 5 | 0.98 | 0.99 | **0.96** | **0.97** |
| Euclidean | 7 | 0.97 | 0.99 | **0.95** | **0.97** |
| Manhattan | 3 | 0.99 | 1.00 | **0.97** | **0.98** |
| Manhattan | 5 | 0.98 | 1.00 | **0.97** | **0.98** |
| Manhattan | 7 | 0.98 | 1.00 | **0.96** | **0.98** |
| Canberra | 3 | 0.95 | 1.00 | **0.91** | **0.95** |
| Canberra | 5 | 0.95 | 0.96 | **0.92** | **0.94** |
| Canberra | 7 | 0.94 | 0.96 | **0.91** | **0.93** |
| Chebyshev | 3 | 0.98 | 0.99 | **0.96** | **0.98** |
| Chebyshev | 5 | 0.97 | 0.99 | **0.94** | **0.97** |
| Chebyshev | 7 | 0.97 | 0.99 | **0.94** | **0.97** |
| Chi-square | 3 | 0.30 | 0.30 | **0.35** | **0.32** |
| Chi-square | 5 | 0.26 | 0.27 | **0.31** | **0.29** |
| Chi-square | 7 | 0.22 | 0.22 | **0.25** | **0.23** |
| Mahalanobis | 3 | 0.98 | 1.00 | **0.95** | **0.97** |
| Mahalanobis | 5 | 0.97 | 0.99 | **0.95** | **0.97** |
| Mahalanobis | 7 | 0.97 | 0.98 | **0.96** | **0.97** |
| Polar Distance | 3 | 0.98 | 0.99 | **0.96** | **0.97** |
| Polar Distance | 5 | 0.97 | 0.97 | **0.96** | **0.96** |
| Polar Distance | 7 | 0.97 | 0.98 | **0.96** | **0.97** |

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.98 | 1.00 | **0.97** | **0.98** |
| Euclidean | 5 | 0.98 | 0.99 | **0.96** | **0.97** |
| Euclidean | 7 | 0.97 | 0.99 | **0.95** | **0.97** |
| Manhattan | 3 | 0.99 | 1.00 | **0.97** | **0.99** |
| Manhattan | 5 | 0.98 | 1.00 | **0.97** | **0.98** |
| Manhattan | 7 | 0.98 | 1.00 | **0.96** | **0.98** |
| Canberra | 3 | 0.96 | 1.00 | **0.93** | **0.96** |
| Canberra | 5 | 0.96 | 0.98 | **0.94** | **0.96** |
| Canberra | 7 | 0.96 | 0.98 | **0.94** | **0.96** |
| Chebyshev | 3 | 0.98 | 1.00 | **0.96** | **0.98** |
| Chebyshev | 5 | 0.97 | 0.99 | **0.95** | **0.97** |
| Chebyshev | 7 | 0.98 | 0.99 | **0.96** | **0.98** |
| Chi-square | 3 | 0.30 | 0.30 | **0.35** | **0.32** |
| Chi-square | 5 | 0.26 | 0.27 | **0.31** | **0.29** |
| Chi-square | 7 | 0.22 | 0.22 | **0.25** | **0.23** |
| Mahalanobis | 3 | 0.98 | 1.00 | **0.96** | **0.98** |
| Mahalanobis | 5 | 0.98 | 0.99 | **0.96** | **0.98** |
| Mahalanobis | 7 | 0.97 | 0.98 | **0.95** | **0.97** |
| Polar Distance | 3 | 0.98 | 1.00 | **0.97** | **0.98** |
| Polar Distance | 5 | 0.97 | 0.99 | **0.94** | **0.97** |
| Polar Distance | 7 | 0.98 | 0.99 | **0.96** | **0.98** |

# Table S2. Performance Comparison on Liver Disease Dataset

This table reports Accuracy (Acc), Precision (Prec), Recall (Rec), and F1-score (F1)
for Classical k-NN (KNN) and Quantum k-NN (QKNN) across k = 3, 5, 7.
Results are presented for the original imbalanced data and after applying SMOTE-ENN.

---

## A. Before Balancing (Imbalanced Data)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.60 | 0.67 | **0.67** | **0.67** |
| Euclidean | 5 | 0.59 | 0.66 | **0.68** | **0.67** |
| Euclidean | 7 | 0.57 | 0.64 | **0.69** | **0.67** |
| Manhattan | 3 | 0.63 | 0.69 | **0.73** | **0.71** |
| Manhattan | 5 | 0.63 | 0.69 | **0.74** | **0.71** |
| Manhattan | 7 | 0.61 | 0.67 | **0.70** | **0.69** |
| Canberra | 3 | 0.63 | 0.70 | **0.69** | **0.69** |
| Canberra | 5 | 0.64 | 0.70 | **0.71** | **0.71** |
| Canberra | 7 | 0.66 | 0.71 | **0.74** | **0.73** |
| Chebyshev | 3 | 0.60 | 0.67 | **0.68** | **0.68** |
| Chebyshev | 5 | 0.58 | 0.65 | **0.68** | **0.67** |
| Chebyshev | 7 | 0.58 | 0.65 | **0.69** | **0.67** |
| Chi-square | 3 | 0.50 | 0.59 | **0.63** | **0.61** |
| Chi-square | 5 | 0.55 | 0.61 | **0.73** | **0.66** |
| Chi-square | 7 | 0.62 | 0.67 | **0.77** | **0.71** |
| Mahalanobis | 3 | 0.61 | 0.68 | **0.69** | **0.69** |
| Mahalanobis | 5 | 0.60 | 0.66 | **0.71** | **0.68** |
| Mahalanobis | 7 | 0.59 | 0.65 | **0.73** | **0.69** |
| Polar Distance | 3 | 0.62 | 0.69 | **0.69** | **0.69** |
| Polar Distance | 5 | 0.63 | 0.69 | **0.72** | **0.71** |
| Polar Distance | 7 | 0.61 | 0.68 | **0.71** | **0.69** |

---

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.59 | 0.67 | **0.67** | **0.67** |
| Euclidean | 5 | 0.59 | 0.66 | **0.68** | **0.67** |
| Euclidean | 7 | 0.58 | 0.65 | **0.70** | **0.67** |
| Manhattan | 3 | 0.61 | 0.68 | **0.69** | **0.68** |
| Manhattan | 5 | 0.63 | 0.69 | **0.72** | **0.70** |
| Manhattan | 7 | 0.62 | 0.68 | **0.71** | **0.70** |
| Canberra | 3 | 0.63 | 0.70 | **0.69** | **0.69** |
| Canberra | 5 | 0.64 | 0.70 | **0.71** | **0.71** |
| Canberra | 7 | 0.65 | 0.70 | **0.76** | **0.73** |
| Chebyshev | 3 | 0.60 | 0.67 | **0.68** | **0.67** |
| Chebyshev | 5 | 0.59 | 0.66 | **0.69** | **0.68** |
| Chebyshev | 7 | 0.59 | 0.66 | **0.70** | **0.68** |
| Chi-square | 3 | 0.50 | 0.59 | **0.63** | **0.61** |
| Chi-square | 5 | 0.55 | 0.61 | **0.73** | **0.66** |
| Chi-square | 7 | 0.55 | 0.61 | **0.73** | **0.66** |
| Mahalanobis | 3 | 0.61 | 0.67 | **0.69** | **0.68** |
| Mahalanobis | 5 | 0.60 | 0.66 | **0.70** | **0.68** |
| Mahalanobis | 7 | 0.59 | 0.65 | **0.71** | **0.68** |
| Polar Distance | 3 | 0.60 | 0.67 | **0.67** | **0.67** |
| Polar Distance | 5 | 0.60 | 0.67 | **0.69** | **0.68** |
| Polar Distance | 7 | 0.59 | 0.66 | **0.71** | **0.68** |

---

## B. After Balancing (SMOTE-ENN)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.88 | 0.90 | **0.90** | **0.85** |
| Euclidean | 5 | 0.84 | 0.84 | **0.74** | **0.78** |
| Euclidean | 7 | 0.80 | 0.79 | **0.67** | **0.72** |
| Manhattan | 3 | 0.87 | 0.87 | **0.80** | **0.83** |
| Manhattan | 5 | 0.83 | 0.82 | **0.72** | **0.77** |
| Manhattan | 7 | 0.78 | 0.79 | **0.61** | **0.69** |
| Canberra | 3 | 0.86 | 0.91 | **0.71** | **0.80** |
| Canberra | 5 | 0.85 | 0.89 | **0.71** | **0.79** |
| Canberra | 7 | 0.83 | 0.85 | **0.68** | **0.76** |
| Chebyshev | 3 | 0.88 | 0.92 | **0.78** | **0.84** |
| Chebyshev | 5 | 0.82 | 0.83 | **0.70** | **0.76** |
| Chebyshev | 7 | 0.77 | 0.75 | **0.62** | **0.68** |
| Chi-square | 3 | 0.50 | 0.38 | **0.39** | **0.38** |
| Chi-square | 5 | 0.49 | 0.36 | **0.36** | **0.36** |
| Chi-square | 7 | 0.45 | 0.32 | **0.35** | **0.34** |
| Mahalanobis | 3 | 0.88 | 0.90 | **0.78** | **0.84** |
| Mahalanobis | 5 | 0.84 | 0.84 | **0.75** | **0.79** |
| Mahalanobis | 7 | 0.82 | 0.82 | **0.68** | **0.75** |
| Polar Distance | 3 | 0.88 | 0.90 | **0.78** | **0.84** |
| Polar Distance | 5 | 0.97 | 0.97 | **0.96** | **0.96** |
| Polar Distance | 7 | 0.81 | 0.80 | **0.70** | **0.74** |

---

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.88 | 0.90 | **0.90** | **0.85** |
| Euclidean | 5 | 0.84 | 0.84 | **0.74** | **0.78** |
| Euclidean | 7 | 0.80 | 0.79 | **0.67** | **0.72** |
| Manhattan | 3 | 0.88 | 0.89 | **0.81** | **0.85** |
| Manhattan | 5 | 0.84 | 0.83 | **0.75** | **0.79** |
| Manhattan | 7 | 0.78 | 0.78 | **0.62** | **0.69** |
| Canberra | 3 | 0.87 | 0.90 | **0.75** | **0.82** |
| Canberra | 5 | 0.87 | 0.90 | **0.77** | **0.83** |
| Canberra | 7 | 0.83 | 0.86 | **0.70** | **0.77** |
| Chebyshev | 3 | 0.90 | 0.92 | **0.81** | **0.86** |
| Chebyshev | 5 | 0.82 | 0.82 | **0.68** | **0.75** |
| Chebyshev | 7 | 0.79 | 0.78 | **0.67** | **0.72** |
| Chi-square | 3 | 0.49 | 0.37 | **0.38** | **0.37** |
| Chi-square | 5 | 0.49 | 0.36 | **0.36** | **0.36** |
| Chi-square | 7 | 0.46 | 0.33 | **0.33** | **0.33** |
| Mahalanobis | 3 | 0.88 | 0.90 | **0.80** | **0.85** |
| Mahalanobis | 5 | 0.85 | 0.84 | **0.77** | **0.80** |
| Mahalanobis | 7 | 0.81 | 0.81 | **0.68** | **0.74** |
| Polar Distance | 3 | 0.89 | 0.90 | **0.81** | **0.85** |
| Polar Distance | 5 | 0.97 | 0.99 | **0.94** | **0.97** |
| Polar Distance | 7 | 0.81 | 0.80 | **0.70** | **0.74** |


# Table S3. Performance Comparison on Obesity Dataset

This table reports Accuracy (Acc), Precision (Prec), Recall (Rec), and F1-score (F1)
for Classical k-NN (KNN) and Quantum k-NN (QKNN) across k = 3, 5, 7.
Results are presented for the original imbalanced data and after applying SMOTE-ENN.

---

## A. Before Balancing (Imbalanced Data)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.87 | 0.92 | **0.96** | **0.94** |
| Euclidean | 5 | 0.86 | 0.88 | **0.96** | **0.92** |
| Euclidean | 7 | 0.82 | 0.87 | **0.98** | **0.92** |
| Manhattan | 3 | 0.79 | 0.91 | **0.91** | **0.91** |
| Manhattan | 5 | 0.86 | 0.94 | **0.94** | **0.94** |
| Manhattan | 7 | 0.89 | 0.96 | **1.00** | **0.98** |
| Canberra | 3 | 0.77 | 0.84 | **0.91** | **0.88** |
| Canberra | 5 | 0.81 | 0.83 | **0.96** | **0.89** |
| Canberra | 7 | 0.81 | 0.84 | **0.98** | **0.90** |
| Chebyshev | 3 | 0.84 | 0.90 | **0.94** | **0.92** |
| Chebyshev | 5 | 0.83 | 0.88 | **0.96** | **0.92** |
| Chebyshev | 7 | 0.80 | 0.86 | **0.91** | **0.89** |
| Chi-square | 3 | 0.28 | 0.28 | **0.28** | **0.28** |
| Chi-square | 5 | 0.32 | 0.33 | **0.32** | **0.32** |
| Chi-square | 7 | 0.31 | 0.32 | **0.36** | **0.34** |
| Mahalanobis | 3 | 0.77 | 0.87 | **0.87** | **0.87** |
| Mahalanobis | 5 | 0.74 | 0.89 | **0.83** | **0.86** |
| Mahalanobis | 7 | 0.69 | 0.84 | **0.87** | **0.85** |
| Polar Distance | 3 | 0.83 | 0.90 | **0.98** | **0.94** |
| Polar Distance | 5 | 0.83 | 0.89 | **1.00** | **0.94** |
| Polar Distance | 7 | 0.76 | 0.85 | **1.00** | **0.92** |

---

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.86 | 0.90 | **0.96** | **0.93** |
| Euclidean | 5 | 0.86 | 0.87 | **0.96** | **0.91** |
| Euclidean | 7 | 0.79 | 0.83 | **0.96** | **0.89** |
| Manhattan | 3 | 0.86 | 0.94 | **0.96** | **0.95** |
| Manhattan | 5 | 0.86 | 0.90 | **0.94** | **0.92** |
| Manhattan | 7 | 0.85 | 0.92 | **0.96** | **0.94** |
| Canberra | 3 | 0.78 | 0.84 | **0.91** | **0.88** |
| Canberra | 5 | 0.82 | 0.86 | **0.91** | **0.89** |
| Canberra | 7 | 0.84 | 0.88 | **0.98** | **0.93** |
| Chebyshev | 3 | 0.87 | 0.92 | **0.96** | **0.94** |
| Chebyshev | 5 | 0.86 | 0.88 | **0.96** | **0.92** |
| Chebyshev | 7 | 0.81 | 0.85 | **0.98** | **0.91** |
| Chi-square | 3 | 0.28 | 0.28 | **0.28** | **0.28** |
| Chi-square | 5 | 0.32 | 0.33 | **0.32** | **0.32** |
| Chi-square | 7 | 0.32 | 0.30 | **0.32** | **0.31** |
| Mahalanobis | 3 | 0.79 | 0.88 | **0.91** | **0.90** |
| Mahalanobis | 5 | 0.79 | 0.89 | **0.89** | **0.89** |
| Mahalanobis | 7 | 0.74 | 0.85 | **0.96** | **0.90** |
| Polar Distance | 3 | 0.83 | 0.88 | **0.96** | **0.92** |
| Polar Distance | 5 | 0.85 | 0.90 | **0.98** | **0.94** |
| Polar Distance | 7 | 0.82 | 0.87 | **1.00** | **0.93** |

---

## B. After Balancing (SMOTE-ENN)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.98 | 0.97 | **1.00** | **0.99** |
| Euclidean | 5 | 0.98 | 0.97 | **1.00** | **0.99** |
| Euclidean | 7 | 0.98 | 0.97 | **1.00** | **0.99** |
| Manhattan | 3 | 0.97 | 0.95 | **1.00** | **0.97** |
| Manhattan | 5 | 0.98 | 0.97 | **1.00** | **0.99** |
| Manhattan | 7 | 0.98 | 0.97 | **1.00** | **0.99** |
| Canberra | 3 | 0.95 | 0.95 | **0.95** | **0.95** |
| Canberra | 5 | 0.95 | 0.90 | **1.00** | **0.95** |
| Canberra | 7 | 0.93 | 0.95 | **0.97** | **0.96** |
| Chebyshev | 3 | 0.98 | 0.97 | **1.00** | **0.99** |
| Chebyshev | 5 | 0.98 | 0.97 | **1.00** | **0.99** |
| Chebyshev | 7 | 0.98 | 0.97 | **1.00** | **0.99** |
| Chi-square | 3 | 0.33 | 0.31 | **0.43** | **0.36** |
| Chi-square | 5 | 0.35 | 0.32 | **0.43** | **0.37** |
| Chi-square | 7 | 0.42 | 0.36 | **0.46** | **0.40** |
| Mahalanobis | 3 | 0.96 | 1.00 | **1.00** | **1.00** |
| Mahalanobis | 5 | 0.93 | 0.95 | **1.00** | **0.97** |
| Mahalanobis | 7 | 0.93 | 0.90 | **1.00** | **0.95** |
| Polar Distance | 3 | 0.95 | 0.95 | **1.00** | **0.97** |
| Polar Distance | 5 | 0.95 | 0.95 | **1.00** | **0.97** |
| Polar Distance | 7 | 0.95 | 0.95 | **1.00** | **0.97** |

---

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.96 | 0.95 | **0.97** | **0.96** |
| Euclidean | 5 | 0.96 | 0.95 | **0.97** | **0.96** |
| Euclidean | 7 | 0.96 | 0.97 | **0.95** | **0.96** |
| Manhattan | 3 | 0.97 | 0.95 | **1.00** | **0.97** |
| Manhattan | 5 | 0.98 | 0.97 | **1.00** | **0.99** |
| Manhattan | 7 | 0.98 | 0.97 | **1.00** | **0.99** |
| Canberra | 3 | 0.97 | 0.95 | **1.00** | **0.97** |
| Canberra | 5 | 0.96 | 0.93 | **1.00** | **0.96** |
| Canberra | 7 | 0.96 | 0.95 | **1.00** | **0.97** |
| Chebyshev | 3 | 0.98 | 0.97 | **1.00** | **0.99** |
| Chebyshev | 5 | 0.98 | 0.97 | **1.00** | **0.99** |
| Chebyshev | 7 | 0.98 | 0.97 | **1.00** | **0.99** |
| Chi-square | 3 | 0.35 | 0.31 | **0.46** | **0.37** |
| Chi-square | 5 | 0.39 | 0.33 | **0.46** | **0.39** |
| Chi-square | 7 | 0.47 | 0.38 | **0.49** | **0.43** |
| Mahalanobis | 3 | 0.95 | 0.95 | **1.00** | **0.97** |
| Mahalanobis | 5 | 0.95 | 0.95 | **1.00** | **0.97** |
| Mahalanobis | 7 | 0.95 | 0.95 | **1.00** | **0.97** |
| Polar Distance | 3 | 0.96 | 0.95 | **1.00** | **0.97** |
| Polar Distance | 5 | 0.97 | 0.97 | **1.00** | **0.99** |
| Polar Distance | 7 | 0.97 | 0.97 | **1.00** | **0.99** |

---


# Table S4. Performance Comparison on Breast Cancer Dataset

This table reports Accuracy (Acc), Precision (Prec), Recall (Rec), and F1-score (F1)
for Classical k-NN (KNN) and Quantum k-NN (QKNN) across k = 3, 5, 7.
Results are presented for the original imbalanced data and after applying SMOTE-ENN.

---

## A. Before Balancing (Imbalanced Data)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.95 | 0.91 | **0.90** | **0.90** |
| Euclidean | 5 | 0.95 | 0.91 | **0.90** | **0.90** |
| Euclidean | 7 | 0.95 | 0.91 | **0.87** | **0.89** |
| Manhattan | 3 | 0.95 | 0.93 | **0.89** | **0.91** |
| Manhattan | 5 | 0.95 | 0.93 | **0.89** | **0.91** |
| Manhattan | 7 | 0.95 | 0.94 | **0.85** | **0.89** |
| Canberra | 3 | 0.91 | 0.84 | **0.81** | **0.82** |
| Canberra | 5 | 0.91 | 0.84 | **0.81** | **0.82** |
| Canberra | 7 | 0.93 | 0.86 | **0.85** | **0.86** |
| Chebyshev | 3 | 0.94 | 0.89 | **0.87** | **0.88** |
| Chebyshev | 5 | 0.94 | 0.89 | **0.87** | **0.88** |
| Chebyshev | 7 | 0.96 | 0.98 | **0.85** | **0.91** |
| Chi-square | 3 | 0.55 | 0.12 | **0.12** | **0.12** |
| Chi-square | 5 | 0.55 | 0.12 | **0.12** | **0.12** |
| Chi-square | 7 | 0.96 | 0.94 | **0.89** | **0.91** |
| Mahalanobis | 3 | 0.94 | 0.93 | **0.82** | **0.87** |
| Mahalanobis | 5 | 0.94 | 0.93 | **0.82** | **0.87** |
| Mahalanobis | 7 | 0.94 | 0.97 | **0.77** | **0.86** |
| Polar Distance | 3 | 0.94 | 0.86 | **0.90** | **0.88** |
| Polar Distance | 5 | 0.94 | 0.90 | **0.86** | **0.88** |
| Polar Distance | 7 | 0.94 | 0.87 | **0.92** | **0.89** |

---

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.81 | 0.66 | **0.50** | **0.57** |
| Euclidean | 5 | 0.81 | 0.66 | **0.50** | **0.57** |
| Euclidean | 7 | 0.83 | 0.80 | **0.42** | **0.55** |
| Manhattan | 3 | 0.95 | 0.93 | **0.89** | **0.91** |
| Manhattan | 5 | 0.95 | 0.93 | **0.89** | **0.91** |
| Manhattan | 7 | 0.95 | 0.93 | **0.85** | **0.89** |
| Canberra | 3 | 0.92 | 0.87 | **0.80** | **0.83** |
| Canberra | 5 | 0.92 | 0.87 | **0.80** | **0.83** |
| Canberra | 7 | 0.92 | 0.90 | **0.78** | **0.84** |
| Chebyshev | 3 | 0.95 | 0.91 | **0.88** | **0.90** |
| Chebyshev | 5 | 0.95 | 0.91 | **0.88** | **0.90** |
| Chebyshev | 7 | 0.96 | 0.95 | **0.88** | **0.91** |
| Chi-square | 3 | 0.55 | 0.12 | **0.12** | **0.12** |
| Chi-square | 5 | 0.55 | 0.12 | **0.12** | **0.12** |
| Chi-square | 7 | 0.60 | 0.04 | **0.03** | **0.04** |
| Mahalanobis | 3 | 0.95 | 0.92 | **0.87** | **0.89** |
| Mahalanobis | 5 | 0.95 | 0.92 | **0.87** | **0.89** |
| Mahalanobis | 7 | 0.94 | 0.96 | **0.80** | **0.87** |
| Polar Distance | 3 | 0.94 | 0.90 | **0.86** | **0.88** |
| Polar Distance | 5 | 0.94 | 0.90 | **0.86** | **0.88** |
| Polar Distance | 7 | 0.94 | 0.90 | **0.84** | **0.87** |

---

## B. After Balancing (SMOTE-ENN)

### Classical k-NN (KNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 1.00 | 0.99 | **1.00** | **1.00** |
| Euclidean | 5 | 0.99 | 0.99 | **1.00** | **0.99** |
| Euclidean | 7 | 0.99 | 0.99 | **1.00** | **0.99** |
| Manhattan | 3 | 0.99 | 0.99 | **1.00** | **1.00** |
| Manhattan | 5 | 0.99 | 0.99 | **1.00** | **0.99** |
| Manhattan | 7 | 0.99 | 0.99 | **1.00** | **0.99** |
| Canberra | 3 | 0.97 | 0.95 | **1.00** | **0.97** |
| Canberra | 5 | 0.97 | 0.94 | **1.00** | **0.97** |
| Canberra | 7 | 0.96 | 0.93 | **1.00** | **0.96** |
| Chebyshev | 3 | 0.99 | 0.99 | **1.00** | **0.99** |
| Chebyshev | 5 | 0.99 | 0.99 | **1.00** | **0.99** |
| Chebyshev | 7 | 0.98 | 0.98 | **0.99** | **0.98** |
| Chi-square | 3 | 0.34 | 0.34 | **0.32** | **0.33** |
| Chi-square | 5 | 0.32 | 0.32 | **0.31** | **0.32** |
| Chi-square | 7 | 0.32 | 0.33 | **0.32** | **0.33** |
| Mahalanobis | 3 | 0.99 | 0.98 | **1.00** | **0.99** |
| Mahalanobis | 5 | 0.98 | 0.98 | **0.99** | **0.98** |
| Mahalanobis | 7 | 0.99 | 0.98 | **0.99** | **0.99** |
| Polar Distance | 3 | 0.99 | 0.97 | **1.00** | **0.99** |
| Polar Distance | 5 | 0.98 | 0.96 | **1.00** | **0.98** |
| Polar Distance | 7 | 0.97 | 0.95 | **1.00** | **0.97** |

---

### Quantum k-NN (QKNN)

| Distance | k | Acc | Prec | **Rec** | **F1** |
|---|---:|---:|---:|---:|---:|
| Euclidean | 3 | 0.89 | 0.86 | **0.93** | **0.90** |
| Euclidean | 5 | 0.86 | 0.83 | **0.91** | **0.87** |
| Euclidean | 7 | 0.84 | 0.84 | **0.85** | **0.85** |
| Manhattan | 3 | 1.00 | 0.99 | **1.00** | **1.00** |
| Manhattan | 5 | 0.99 | 0.99 | **1.00** | **0.99** |
| Manhattan | 7 | 0.99 | 0.99 | **1.00** | **0.99** |
| Canberra | 3 | 0.99 | 0.98 | **1.00** | **0.99** |
| Canberra | 5 | 0.98 | 0.98 | **0.99** | **0.98** |
| Canberra | 7 | 0.98 | 0.96 | **1.00** | **0.98** |
| Chebyshev | 3 | 1.00 | 0.99 | **1.00** | **1.00** |
| Chebyshev | 5 | 0.99 | 0.99 | **1.00** | **0.99** |
| Chebyshev | 7 | 0.99 | 0.98 | **0.99** | **0.99** |
| Chi-square | 3 | 0.34 | 0.34 | **0.32** | **0.33** |
| Chi-square | 5 | 0.32 | 0.32 | **0.31** | **0.32** |
| Chi-square | 7 | 0.32 | 0.33 | **0.32** | **0.33** |
| Mahalanobis | 3 | 1.00 | 0.99 | **1.00** | **1.00** |
| Mahalanobis | 5 | 0.99 | 0.99 | **1.00** | **0.99** |
| Mahalanobis | 7 | 1.00 | 0.99 | **1.00** | **1.00** |
| Polar Distance | 3 | 0.99 | 0.99 | **1.00** | **0.99** |
| Polar Distance | 5 | 0.99 | 0.99 | **1.00** | **0.99** |
| Polar Distance | 7 | 0.99 | 0.99 | **1.00** | **0.99** |

---
