# 📊 Portfolio Performance Dashboard

## 🚀 Overview
This **Portfolio Performance Dashboard** is a **data-driven analytics tool** that:
 - Fetches and stores stock price data 📈  
 - nalyzes portfolio performance of hypothetical symbols using **Monte Carlo simulations**
 - Optimizes portfolios for **Max Sharpe Ratio** and **Min Volatility**
 - Provides **interactive visualizations** via **Streamlit**
 - Please note it's for fun and educational purposes and mostly just to explore data analysis.
In simple terms, it's a quick and simple demonstration of the power of using SQLite with Python and a few other libraries to analyze data!

## 📂 Project Structure
portfolio-dashboard/
│── .gitignore
│── README.md
│── requirements.txt
│── src/
│   ├── app.py               # Streamlit Dashboard
│   ├── analytics.py         # Monte Carlo Optimization
│   ├── data_cleaning.py     # Data Cleaning Functions
│   ├── data_fetch.py        # Fetches Stock Data
│   ├── database.py          # Manages SQLite Database
│── database/
│   ├── portfolio.db         # SQLite Database
│── .streamlit/              # Streamlit Deployment Config

## 🛠 Installation
1. Clone the repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/portfolio-dashboard.git
cd portfolio-dashboard
2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run the Streamlit app:
streamlit run src/app.py

## Features
- Live Data Fetching from Yahoo Finance
- Cumulative Portfolio Performance Chart
- Sharpe Ratio Comparison with S&P 500
- SQLite Database Storage for Historical Data

🚀 Developed by Andrew Zimmerman
📧 Contact: andrewszimmerman@outlook.com