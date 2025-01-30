import numpy as np
import pandas as pd
from data_cleaning import clean_data

def monte_carlo_optimization(returns, risk_free_rate=0.02, num_portfolios=10000):
    """
    Monte Carlo Simulation to approximate the Maximum Sharpe Ratio portfolio.
    """
    num_assets = returns.shape[1]
    results = np.zeros((3, num_portfolios))
    weight_array = []

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    for i in range(num_portfolios):
        # Generate random weights
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)  # Normalize to sum to 1
        weight_array.append(weights)

        # Compute portfolio return and volatility
        port_return = np.dot(weights, mean_returns)
        port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        # Compute Sharpe Ratio
        sharpe_ratio = (port_return - risk_free_rate) / port_volatility if port_volatility > 0 else 0

        results[0, i] = port_return
        results[1, i] = port_volatility
        results[2, i] = sharpe_ratio

    # Find the best Sharpe Ratio portfolio
    max_sharpe_idx = np.argmax(results[2])
    optimal_sharpe_weights = weight_array[max_sharpe_idx]

    # Find the minimum volatility portfolio
    min_vol_idx = np.argmin(results[1])
    min_vol_weights = weight_array[min_vol_idx]

    return optimal_sharpe_weights, min_vol_weights

def optimize_portfolio(symbols, risk_free_rate=0.02):
    """Optimize portfolio allocation using Monte Carlo Simulation."""
    prices, returns = clean_data(symbols)

    if returns.empty:
        raise ValueError("❌ Error: No valid return data found for optimization.")

    print("Running Monte Carlo Optimization...")
    max_sharpe_weights, min_vol_weights = monte_carlo_optimization(returns, risk_free_rate)

    return {
        "Equal Weight": np.ones(len(symbols)) / len(symbols),
        "Max Sharpe": max_sharpe_weights,
        "Min Volatility": min_vol_weights,
    }

if __name__ == "__main__":
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "TLT"]
    weights = optimize_portfolio(symbols)
    print("Portfolio Optimization Results:", weights)
