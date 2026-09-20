import pandas as pd
from xgboost import XGBClassifier

def get_feature_importance(model: XGBClassifier, feature_names: list[str]) -> pd.Series:
    importance = pd.Series(model.feature_importances_, index=feature_names, name="Importance")
    importance = importance.sort_values(ascending=False)

    return importance