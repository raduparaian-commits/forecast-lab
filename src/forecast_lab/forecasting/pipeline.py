import torch
import pandas as pd

def create_context(df: pd.DataFrame, context_length: int) -> torch.Tensor:
    close_prices = (df["Close"].iloc[-context_length:].to_numpy())

    context = torch.tensor(close_prices, dtype=torch.float32)

    context = context.reshape(1, 1, -1)

    return context