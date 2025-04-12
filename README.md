
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
![{33BD0D7C-B333-4821-99B7-A353C8905BFB}](https://github.com/user-attachments/assets/af4209e0-479d-4e82-8ae4-e2dc6404106a)

> 📈 Visual Insights
![{881DD954-A1EC-4BAE-A943-BF9CE04C2792}](https://github.com/user-attachments/assets/bf6c593e-a67b-4807-a4a7-aff01f33a1c0)
![{9EB16BFA-BF7C-4C11-B7A4-EAC47D3CAF16}](https://github.com/user-attachments/assets/1f03797c-b83e-4d79-9dc3-6699c46a8454)
![{4B697420-1C1A-4A8C-9488-4E3842719ADA}](https://github.com/user-attachments/assets/eb3dc45f-26a4-4513-8cb3-7c9042877632)

> 💡 Action Suggestions
![{208A0391-5895-4039-9982-C124B03D48AB}](https://github.com/user-attachments/assets/15fb03a3-2398-4c94-9dfb-af7e5e1c4e4b)

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
