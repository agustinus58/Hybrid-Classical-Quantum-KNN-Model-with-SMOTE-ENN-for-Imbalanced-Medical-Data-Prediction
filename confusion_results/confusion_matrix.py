import os
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def save_confusion_matrix(
    y_true,
    y_pred,
    model_name,
    dataset_name,
    scenario,
    save_dir,
    normalize=False
):
    """
    Save confusion matrix as a PNG file.

    Parameters
    ----------
    y_true : array-like
        True class labels
    y_pred : array-like
        Predicted class labels
    model_name : str
        Model name (e.g., 'KNN', 'QKNN')
    dataset_name : str
        Dataset name (e.g., 'Pima', 'Liver', 'Obesity', 'BreastCancer')
    scenario : str
        Scenario description (e.g., 'Imbalanced', 'SMOTE-ENN')
    save_dir : str
        Root directory to save confusion matrix images
    normalize : bool, optional
        If True, normalize confusion matrix (default: False)
    """

    os.makedirs(save_dir, exist_ok=True)

    cm = confusion_matrix(
        y_true,
        y_pred,
        normalize="true" if normalize else None
    )

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)

    fig, ax = plt.subplots(figsize=(5, 5))
    disp.plot(
        ax=ax,
        cmap="Blues",
        colorbar=False,
        values_format=".2f" if normalize else "d"
    )

    title = f"Confusion Matrix - {model_name}\n{dataset_name} ({scenario})"
    ax.set_title(title, fontsize=11)

    plt.tight_layout()

    filename = f"{model_name.lower()}_{scenario.lower().replace(' ', '_')}.png"
    save_path = os.path.join(save_dir, filename)

    plt.savefig(save_path, dpi=300)
    plt.close()

    print(f"[INFO] Confusion matrix saved to: {save_path}")

from utils.confusion_matrix import save_confusion_matrix

save_confusion_matrix(
    y_true=y_test,
    y_pred=y_pred_knn,
    model_name="KNN",
    dataset_name="Pima Indian Diabetes",
    scenario="Imbalanced",
    save_dir="confusion_results/Pima",
    normalize=False
)

save_confusion_matrix(
    y_true=y_test,
    y_pred=y_pred_qknn,
    model_name="QKNN",
    dataset_name="Pima Indian Diabetes",
    scenario="Imbalanced",
    save_dir="confusion_results/Pima",
    normalize=False
)

save_confusion_matrix(
    y_true=y_test,
    y_pred=y_pred_knn_bal,
    model_name="KNN",
    dataset_name="Pima Indian Diabetes",
    scenario="SMOTE-ENN",
    save_dir="confusion_results/Pima",
    normalize=True
)

save_confusion_matrix(
    y_true=y_test,
    y_pred=y_pred_qknn_bal,
    model_name="QKNN",
    dataset_name="Pima Indian Diabetes",
    scenario="SMOTE-ENN",
    save_dir="confusion_results/Pima",
    normalize=True
)
