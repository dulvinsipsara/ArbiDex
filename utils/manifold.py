import requests
import pandas as pd

def get_manifold_data():
    url = "https://api.manifold.markets/v0/markets"
    try:
        r = requests.get(url)
        data = r.json()

        records = []
        for market in data:
            if market["outcomeType"] == "BINARY":
                records.append({
                    "platform": "Manifold",
                    "ticker": market["id"][:8],
                    "title": market["question"],
                    "yes_price": float(market.get("probability", 0)),
                    "url": f"https://manifold.markets/{market['slug']}"
                })

        return pd.DataFrame(records)

    except Exception as e:
        print("Error fetching Manifold data:", e)
        return pd.DataFrame()
