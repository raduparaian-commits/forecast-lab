import torch
from dataclasses import dataclass

@dataclass
class Forecast:
    values = torch.Tensor
    prediction_length: int