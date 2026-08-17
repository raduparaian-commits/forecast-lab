import torch
from forecast_lab.forecasting import Forecast

class NaiveForecaster:
    def predict(self, context: torch.Tensor, prediction_length: int) -> Forecast:
        last_value = context[:, :, -1:]

        forecast = last_value.repeat(1, 1, prediction_length)

        return Forecast(values=forecast, prediction_length=prediction_length)