import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.replace("\n", " ").replace("\r", " ").strip()
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def shorten(text, max_len=80):
    if not isinstance(text, str):
        return ""
    text = text if len(text) <= max_len else text[:max_len].strip() + "..."
    text = text.replace("_", "\\_").replace("*", "\\*").replace("`", "\\`")
    return text

def generate_action_suggestions(df):
    suggestions = {
        "Traders": [],
        "Researchers": [],
        "Bot Developers": []
    }

    for _, row in df.iterrows():
        title1 = clean_text(row["title_1"])
        title2 = clean_text(row["title_2"])
        if title1.strip() == title2.strip():
            continue

        gap = round(row["price_gap"], 2)
        sim = round(row["similarity"], 1)
        theme = row.get("theme_1", "Other")

        title1_short = shorten(title1)
        title2_short = shorten(title2)

        if gap >= 0.1 and sim >= 80:
            suggestions["Traders"].append(
                f"💰 Arbitrage between: '{title1_short}' ↔ '{title2_short}' (Gap: {gap}, Sim: {sim}%)")

        if gap >= 0.08 and theme in ["Politics", "AI / Tech"]:
            suggestions["Researchers"].append(
                f"🔍 Sentiment drift in '{theme}' → '{title1_short}' vs '{title2_short}' (Gap: {gap})")

        if gap >= 0.12 and sim >= 85:
            suggestions["Bot Developers"].append(
                f"🤖 Trigger bot (Gap >12%, Sim >85): '{title1_short}' vs '{title2_short}'")

    return suggestions
