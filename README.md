
# 🧠 ArbiDex: Market Arbitrage Opportunity Finder

ArbiDex is a Streamlit-based analytics dashboard that detects and visualizes arbitrage opportunities between similar prediction markets on **Manifold**. It automatically fetches market data, detects mismatches using fuzzy logic, saves historical data with **SQLite + SQLAlchemy**, and provides insightful visualizations for traders, researchers, and bot developers.

## 🚀 Features

- 🔄 Live market data from Manifold
- 🧠 Self-arbitrage detection with fuzzy string matching
- 📊 Visualizations: Top Gaps, Similarity vs Gap, Theme Trends, Price Comparison
- 🗃️ Historical database storage (SQLite)
- 📅 Weekly trends by arbitrage theme
- 💡 Actionable recommendations by user type
- 🧰 Sidebar filters, refresh, and past data recall

## 📷 Screenshots

> 📡 Market Data (Expandable)

![market](https://via.placeholder.com/800x300?text=Market+Data)

> 📈 Visual Insights

![charts](https://via.placeholder.com/800x300?text=Charts+Overview)

> 💡 Action Suggestions

![recommend](https://via.placeholder.com/800x300?text=Recommendations)

## 🛠️ Tech Stack

- `Streamlit` for UI
- `Pandas` for data manipulation
- `Altair` for plotting
- `RapidFuzz` for similarity scoring
- `SQLAlchemy + SQLite` for storage

## 📦 Folder Structure

```
ArbiDex/
├── app.py
├── utils/
│   ├── manifold.py
│   ├── arbitrage.py
│   ├── action_suggestions.py
│   ├── database.py
├── arbidex.db
├── requirements.txt
```

## 📄 Requirements

Install via:

```bash
pip install -r requirements.txt
```

## 🧪 Run Locally

```bash
streamlit run app.py
```

## 📬 Contact

Made by [@alexandertiopan1212](https://github.com/alexandertiopan1212) – feel free to fork or star!

---
**ArbiDex** is an experimental analytics tool, not financial advice.
