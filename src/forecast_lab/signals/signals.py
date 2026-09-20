import numpy as np
import pandas as pd

def generate_signals(class_probabilities: pd.DataFrame, macro_trend: pd.Series, probability_threshold: float | int, signal_class: int, neutral_class: int, trend_value: int) -> pd.Series:
    if not 0 <= probability_threshold <= 1:
        raise ValueError("probability_threshold must be between zero and one")

    probability_condition = class_probabilities[signal_class] >= probability_threshold
    trend_condition = macro_trend == trend_value
    signal_condition = probability_condition & trend_condition
    signal_values = np.where(signal_condition, signal_class, neutral_class)
    signals = pd.Series(signal_values, index=class_probabilities.index, name="Signal")

    return signals