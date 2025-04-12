from rapidfuzz import fuzz
import pandas as pd

def find_self_arbitrage_opportunities(df, threshold=70, price_gap=0.1):
    opportunities = []

    for i, row1 in df.iterrows():
        for j, row2 in df.iterrows():
            if i >= j:
                continue  # jangan bandingin diri sendiri dan yang udah dicek

            similarity = fuzz.token_sort_ratio(row1['title'], row2['title'])

            if similarity >= threshold:
                gap = abs(row1['yes_price'] - row2['yes_price'])

                if gap >= price_gap:
                    opportunities.append({
                        "title_1": row1['title'],
                        "title_2": row2['title'],
                        "price_1": row1['yes_price'],
                        "price_2": row2['yes_price'],
                        "price_gap": round(gap, 4),
                        "similarity": similarity,
                        "url_1": row1.get("url", ""),
                        "url_2": row2.get("url", "")
                    })

    return pd.DataFrame(opportunities)


def classify_theme(title):
    title = title.lower()
    if any(k in title for k in ["ai", "artificial", "model", "chatgpt"]):
        return "AI / Tech"
    elif any(k in title for k in ["trump", "biden", "election", "vote", "senate", "republican"]):
        return "Politics"
    elif any(k in title for k in ["stock", "inflation", "recession", "finance", "economy", "interest"]):
        return "Finance"
    elif any(k in title for k in ["bitcoin", "crypto", "ethereum", "blockchain"]):
        return "Crypto"
    elif any(k in title for k in ["covid", "vaccine", "health", "labcorp", "metabolomix"]):
        return "Health"
    else:
        return "Other"
