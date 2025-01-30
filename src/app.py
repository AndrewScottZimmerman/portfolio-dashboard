import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from analytics import optimize_portfolio
from data_cleaning import clean_data
from database import get_historical_performance

# Streamlit UI
st.set_page_config(page_title="Portfolio Dashboard", layout="wide")

st.title("📊 Portfolio Performance Dashboard")

# User selects stocks
symbols = st.multiselect("Select Stocks", ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "TLT"], default=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "TLT"])

if symbols:
    # Fetch & clean data
    prices, returns = clean_data(symbols)
    benchmark_prices, benchmark_returns = clean_data(["^GSPC"])  # Get S&P 500 data
    
    # Optimize Portfolio
    weights = optimize_portfolio(symbols)

    # ---- Portfolio Allocation ----
    st.subheader("📌 Portfolio Allocation")
    col1, col2, col3 = st.columns(3)

    for i, (strategy, w) in enumerate(weights.items()):
        df_weights = pd.DataFrame({"Stock": symbols, "Weight": w})

        fig = px.pie(df_weights, names="Stock", values="Weight", title=f"{strategy} Allocation")
        if i == 0:
            col1.plotly_chart(fig, use_container_width=True)
        elif i == 1:
            col2.plotly_chart(fig, use_container_width=True)
        else:
            col3.plotly_chart(fig, use_container_width=True)

    # ---- Historical Performance ----
    st.subheader("📈 Portfolio vs. S&P 500 Performance")
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for strategy, w in weights.items():
        strat_returns = (returns * w).sum(axis=1).cumsum()
        ax.plot(strat_returns, label=strategy)
    
    # Add S&P 500 line
    if not benchmark_returns.empty:
        benchmark_cumulative = benchmark_returns.cumsum()
        ax.plot(benchmark_cumulative, label="S&P 500", linestyle="dashed", color="black")

    ax.legend()
    ax.set_title("Cumulative Portfolio Returns vs. S&P 500")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Return")
    st.pyplot(fig)

    # ---- Sharpe Ratio vs. Benchmark ----
    st.subheader("📊 Sharpe Ratio Comparison")
    benchmark_sharpe = benchmark_returns.mean().values[0] / benchmark_returns.std().values[0]

    sharpe_ratios = {s: (returns.mean() @ w) / (returns.std() @ w) for s, w in weights.items()}
    sharpe_ratios["S&P 500"] = benchmark_sharpe

    df_sharpe = pd.DataFrame.from_dict(sharpe_ratios, orient="index", columns=["Sharpe Ratio"])
    df_sharpe.reset_index(inplace=True)
    df_sharpe.rename(columns={"index": "Strategy"}, inplace=True)

    fig = px.bar(df_sharpe, x="Strategy", y="Sharpe Ratio", title="Sharpe Ratio Comparison", color="Sharpe Ratio")
    st.plotly_chart(fig, use_container_width=True)

    # ---- Historical Portfolio Performance ----
    st.subheader("📊 Portfolio Performance Over Time")
    df_perf = get_historical_performance()
    if not df_perf.empty:
        st.line_chart(df_perf.pivot(index="date", columns="strategy", values="cumulative_return"))
    else:
        st.write("No historical data available yet.")
