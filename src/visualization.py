import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_performance(prices, returns, cumulative_returns):
    """
    Generate key portfolio visualizations.
    
    Parameters:
        prices (pd.DataFrame): Cleaned historical prices.
        returns (pd.DataFrame): Daily returns.
        cumulative_returns (pd.Series): Cumulative returns of the portfolio.
    """
    plt.figure(figsize=(12, 6))
    
    # Plot cumulative returns
    cumulative_returns.plot(title="Portfolio Cumulative Returns", linewidth=2)
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")
    plt.grid()
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 5))
    sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Asset Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    prices = pd.read_csv("../data/cleaned_prices.csv", index_col=0, parse_dates=True)
    returns = pd.read_csv("../data/daily_returns.csv", index_col=0, parse_dates=True)
    
    # Load portfolio cumulative returns
    from analytics import calculate_portfolio_metrics
    metrics = calculate_portfolio_metrics(returns)
    
    plot_performance(prices, returns, metrics["cumulative_returns"])