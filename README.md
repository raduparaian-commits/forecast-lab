# Forecast Lab

Forecast Lab is a machine learning project for predicting cryptocurrency prices. It currently focuses on **Bitcoin (BTC)**, with **XRP** and **ETH** planned as the project expands.

Datasets are pulled directly from **Binance** via a download script, and predictions are made using a growing set of models, from simple baselines to foundation time-series models.

## Models

- **Naive Baseline** — a simple reference model used to sanity-check whether the more complex models are actually adding value.
- **XGBoost** — a non-foundation baseline trained on standard technical indicators, including but not limited to:
  - RSI (Relative Strength Index)
  - Bollinger Bands
  - Predictions are framed using the **triple barrier method**.
- **Chronos** — the current primary model, a foundation time-series model.
  - Planned additions: **Lag-Llama** and **custom transformer** architectures.

## Evaluation

Model performance is assessed using:

- Mean Absolute Error (MAE)
- Feature importance
- Backtesting
- Confusion matrices
- Classification reports

## Roadmap

- [ ] Expand data coverage to XRP and ETH
- [ ] Integrate Lag-Llama
- [ ] Build and evaluate custom transformer models
- [ ] Expand backtesting framework across all assets

## Data

Historical price data is downloaded directly from Binance using the included data script.

## Getting Started

Setup and installation instructions coming soon

## Disclaimer

This project is for research and educational purposes only. Nothing here constitutes financial advice.