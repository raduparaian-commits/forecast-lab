import numpy as np
import pandas as pd

def run_backtest(df: pd.DataFrame, initial_balance: float | int, position_size: float | int, trading_fee: float | int, take_profit_pct: float | int, stop_loss_pct: float | int, signal_class: int) -> tuple[pd.Series, pd.DataFrame, dict[str, float | int]]:
    signal_rows = df["Signal"] == signal_class
    trades = df.loc[signal_rows, ["Target"]].copy()
    fee = position_size * trading_fee
    trades["Signal"] = signal_class
    win_condition = trades["Target"] == 1
    loss_condition = trades["Target"] == -1
    trades["Result"] = np.select([win_condition, loss_condition], ["Win", "Loss"], default="Timeout")
    trades["Gross_PnL"] = np.select([win_condition, loss_condition], [position_size * take_profit_pct, -(position_size * stop_loss_pct)], default=0.0)
    trades["Fees"] = fee * 2
    trades["Net_PnL"] = trades["Gross_PnL"] - trades["Fees"]
    cumulative_pnl = trades["Net_PnL"].cumsum()
    trades["Balance"] = initial_balance + cumulative_pnl

    balance_changes = pd.Series(0.0, index=df.index)
    balance_changes.loc[trades.index] = trades["Net_PnL"]
    equity_values = initial_balance + balance_changes.cumsum()
    equity_curve = pd.Series([initial_balance] + equity_values.tolist(), name="Equity")
    equity_array = equity_curve.to_numpy(dtype=float)
    peak = np.maximum.accumulate(equity_array)
    drawdown = (equity_array - peak) / peak
    max_drawdown = drawdown.min()
    max_drawdown_pct = float(max_drawdown * 100)

    total_trades = len(trades)
    wins = int((trades["Result"] == "Win").sum())
    losses = int((trades["Result"] == "Loss").sum())
    timeouts = int((trades["Result"] == "Timeout").sum())
    gross_profit = float(trades.loc[trades["Gross_PnL"] > 0, "Gross_PnL"].sum())
    gross_loss = float(-trades.loc[trades["Gross_PnL"] < 0, "Gross_PnL"].sum())
    final_balance = float(equity_curve.iloc[-1])
    net_profit = final_balance - initial_balance
    metrics = {
        "initial_balance": initial_balance,
        "final_balance": final_balance,
        "net_profit": net_profit,
        "total_return_pct": (net_profit / initial_balance) * 100,
        "total_trades": total_trades,
        "wins": wins,
        "losses": losses,
        "timeouts": timeouts,
        "win_rate_pct": (wins / total_trades * 100) if total_trades else 0.0,
        "gross_profit": gross_profit,
        "gross_loss": gross_loss,
        "total_fees": float(trades["Fees"].sum()),
        "average_net_trade": float(trades["Net_PnL"].mean()) if total_trades else 0.0,
        "profit_factor": gross_profit / gross_loss if gross_loss else 0.0,
        "max_drawdown_pct": max_drawdown_pct
    }

    return equity_curve, trades, metrics