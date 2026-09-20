import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

def get_classification_report(y_true: pd.Series | np.ndarray, y_pred: pd.Series | np.ndarray, labels: list[int], target_names: list[str]) -> str:
    report = classification_report(y_true, y_pred, labels=labels, target_names=target_names, zero_division=0)

    return report

def get_confusion_matrix(y_true: pd.Series | np.ndarray, y_pred: pd.Series | np.ndarray, labels: list[int]) -> np.ndarray:
    matrix = confusion_matrix(y_true, y_pred, labels=labels)

    return matrix