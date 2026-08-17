# **Forecasting Overview**

## **Goal**

Forecast the next 60 one-minute closing prices using only information available when the current one-minute candle has closed.

## **Asset & Frequency**

- Asset: BTC/USD + other crypto later
- Frequency: 1 minute
- Decision time: Immediately after each one-minute candle closes

## **Model Input**

For every prediction time t, the model receives the previous 512 completed one-minute candles.

The model must not receive any data from after time t.

## **Prediction Target**

The model predicts the closing-price for the next 60 minutes:

- Close(t + 1)
- Close(t + 2)
- ...
- Close(t + 60)

## **First Baseline**

The naïve baseline predicts that every future closing price equals the most recent known closing price:

prediction = Close(t)

## **Evaluation Principle**

All models will be evaluated with walk-forward testing.

At every test point, a model can only train on data from before that point. The final test period will remain untouched until the project is complete.