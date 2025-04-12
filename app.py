import streamlit as st
import pandas as pd
import altair as alt

from utils.manifold import get_manifold_data
from utils.arbitrage import find_self_arbitrage_opportunities, classify_theme
from utils.action_suggestions import generate_action_suggestions
from utils.database import (
    save_arbitrage_to_db,
    load_latest_arbitrage,
    load_weekly_theme_trends
)

# --- Streamlit page config
st.set_page_config(page_title="ArbiDex Dashboard", layout="wide")

# --- Stylish header
st.markdown("""
<div style='background-color:#F0F2F6;padding:20px 30px;border-radius:15px;margin-bottom:20px'>
    <h2 style='margin-bottom:10px;'>🧠 ArbiDex Dashboard</h2>
    <p style='margin:0;color:#444;'>A live insight platform to monitor arbitrage gaps between prediction markets. Powered by Manifold & SQLite backend.</p>
</div>
""", unsafe_allow_html=True)

st.title("🧠 ArbiDex: Market Arbitrage Opportunity Finder")
st.caption("Track mismatches between similar Manifold prediction markets.")

# --- Refresh Button
if "refresh" not in st.session_state:
    st.session_state.refresh = False
if st.button("🔁 Refresh Data"):
    st.session_state.refresh = not st.session_state.refresh

# --- Sidebar
st.sidebar.header("🧰 Options")
if st.sidebar.button("📂 Load Past Arbitrage"):
    st.subheader("📜 Last Saved Arbitrage (from DB)")
    past_df = load_latest_arbitrage()
    st.dataframe(past_df, use_container_width=True)

# --- Load Market Data
st.markdown("## 📡 Market Data")
if st.session_state.refresh:
    st.toast("Refreshing data...", icon="🔄")

manifold_df = get_manifold_data()

with st.expander("🔍 Click to expand raw market data from Manifold"):
    st.dataframe(manifold_df if not manifold_df.empty else pd.DataFrame(), use_container_width=True)

# --- Arbitrage Detection
st.markdown("## 💸 Self-Arbitrage Opportunities")

if not manifold_df.empty:
    arb_df = find_self_arbitrage_opportunities(manifold_df)

    if not arb_df.empty:
        st.success("⚡ Self-arbitrage opportunities detected!")
        arb_df["theme_1"] = arb_df["title_1"].apply(classify_theme)

        # --- Filter
        st.sidebar.header("📊 Filter Arbitrage")
        min_gap = st.sidebar.slider("Minimum Price Gap", 0.05, 0.5, 0.1, step=0.01)
        min_sim = st.sidebar.slider("Minimum Similarity", 70, 100, 80)

        filtered_df = arb_df[(arb_df["price_gap"] >= min_gap) & (arb_df["similarity"] >= min_sim)]

        st.markdown("### 🎯 Filtered Arbitrage Opportunities")
        col_a, col_b = st.columns(2)
        col_a.metric("Opportunities", len(filtered_df))
        col_b.metric("Avg. Price Gap", f"{filtered_df['price_gap'].mean():.2%}" if not filtered_df.empty else "–")

        st.dataframe(filtered_df, use_container_width=True)

        save_arbitrage_to_db(filtered_df)

        if not filtered_df.empty:
            # --- Charts
            st.markdown("### 📊 Visual Insights")
            st.subheader("Top Price Gaps")
            st.altair_chart(alt.Chart(filtered_df).mark_bar().encode(
                x="price_gap:Q",
                y=alt.Y("title_1:N", sort='-x'),
                color=alt.Color("similarity:Q", scale=alt.Scale(scheme='blues')),
                tooltip=["title_1", "title_2", "price_gap", "similarity"]
            ).properties(width=900, height=400))

            st.subheader("Similarity vs Price Gap")
            st.altair_chart(alt.Chart(filtered_df).mark_circle(size=100).encode(
                x="similarity:Q",
                y="price_gap:Q",
                tooltip=["title_1", "title_2", "price_gap", "similarity"]
            ).interactive().properties(width=800, height=400))

            st.subheader("Market Price Comparison")
            melted = pd.melt(filtered_df[["title_1", "price_1", "price_2"]], id_vars="title_1", var_name="type", value_name="price")
            st.altair_chart(alt.Chart(melted).mark_bar().encode(
                x="price:Q",
                y=alt.Y("title_1:N", sort='-x'),
                color="type:N",
                tooltip=["title_1", "type", "price"]
            ).properties(width=900, height=400))

            st.subheader("Arbitrage Count by Theme")
            theme_count = filtered_df["theme_1"].value_counts().reset_index()
            theme_count.columns = ["Theme", "Count"]
            st.altair_chart(alt.Chart(theme_count).mark_bar().encode(
                x="Count:Q",
                y=alt.Y("Theme:N", sort='-x'),
                color="Theme:N"
            ).properties(width=600, height=300))

            # --- Actionable Insights
            st.markdown("### 💡 Recommended Actions")
            actions = generate_action_suggestions(filtered_df)
            for role, tips in actions.items():
                st.markdown(f"**👤 {role}**")
                if tips:
                    for t in tips[:3]:
                        st.markdown(f"- {t}")
                else:
                    st.markdown("*No current recommendation.*")

# --- Business Insights
st.markdown("### 📈 Business Insight & Strategy")
st.markdown("""
- **Top Gainers**: Gaps >10% show pricing inefficiencies, good for scalping or sentiment arbitrage.
- **Clustering Themes**: Similar markets often revolve around elections, crypto, AI. These are high-traffic, volatile prediction areas.
- **Trade Strategy**: Enter opposing positions on both markets when confident the prices will converge. Use similarity score >80 as threshold.
""")

st.markdown("### 🎯 Arbitrage Themes Breakdown")
st.markdown("""
- **Most Common Arbitrage Themes**:
    - 🔮 *AI & Tech*: Buzz-heavy but often diverging in prediction probability.
    - 🗳️ *Politics*: High sentiment volatility creates frequent arbitrage.
    - 💰 *Finance*: Market moves lag behind macro news releases.
- **Recommendation**:
    - Fokusin bot lo ke AI dan Politics buat yield arbitrase tertinggi.
    - Bisa juga auto-trade kalau gap >10% dan similarity >85.
""")

# --- Weekly Trends
st.markdown("### 📅 Weekly Arbitrage Trends")
theme_trends_df = load_weekly_theme_trends()

if not theme_trends_df.empty:
    st.write("Volume arbitrage per tema (mingguan)")
    st.altair_chart(alt.Chart(theme_trends_df).mark_line(point=True).encode(
        x=alt.X("week:T", title="Week"),
        y=alt.Y("total:Q", title="Total Arbitrage"),
        color="theme_1:N",
        tooltip=["week", "theme_1", "total"]
    ).properties(width=900, height=400))
else:
    st.info("No trend data available yet.")
