import torch
from chronos import Chronos2Pipeline
from forecast_lab.config import HF_TOKEN
from forecast_lab.forecasting import Forecast

class ChronosForecaster:
    def __init__(self, model_name: str = "amazon/chronos-2") -> None:
        self.pipeline = Chronos2Pipeline.from_pretrained(model_name, device_map="auto", token=HF_TOKEN)

    def predict(self, context: torch.Tensor, prediction_length: int,) -> Forecast:
        forecast = self.pipeline.predict(context, prediction_length=prediction_length)

        return Forecast(values=forecast[0], prediction_length=prediction_length)