from time import perf_counter
from typing import Any

import pandas as pd
from sklearn.utils.class_weight import compute_sample_weight
from xgboost import XGBClassifier

def train_xgb_classifier(X_train: pd.DataFrame, y_train: pd.Series, model_params: dict[str, Any]) -> XGBClassifier:
    sample_weights = compute_sample_weight(class_weight="balanced", y=y_train)
    model = XGBClassifier(**model_params)

    start_time = perf_counter()
    model.fit(X_train, y_train, sample_weight=sample_weights)
    end_time = perf_counter()

    print(f"XGBClassifier training took {end_time - start_time:.2f} seconds.")

    return model


def predict_classes(model: XGBClassifier, features: pd.DataFrame) -> pd.Series:
    predicted_classes = model.predict(features)
    predictions = pd.Series(predicted_classes, index=features.index, name="Prediction")

    return predictions


def predict_probabilities(model: XGBClassifier, features: pd.DataFrame) -> pd.DataFrame:
    probabilities = model.predict_proba(features)
    probability_data = pd.DataFrame(probabilities, index=features.index, columns=model.classes_)

    return probability_data