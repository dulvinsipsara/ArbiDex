from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

# Create or connect to SQLite database
engine = create_engine("sqlite:///arbidex.db", echo=False)

def save_arbitrage_to_db(df, table_name="arbitrage"):
    """Save filtered arbitrage DataFrame to SQLite database with timestamp."""
    if not df.empty:
        df = df.copy()
        df["saved_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.to_sql(table_name, con=engine, if_exists="append", index=False)

def load_latest_arbitrage(limit=100, table_name="arbitrage"):
    """Load the latest saved arbitrage records from the database."""
    query = f"SELECT * FROM {table_name} ORDER BY ROWID DESC LIMIT {limit}"
    return pd.read_sql(query, con=engine)

def load_weekly_theme_trends(table_name="arbitrage"):
    """Load grouped weekly arbitrage counts per theme from the database."""
    query = f'''
        SELECT 
            strftime('%Y-%W', saved_at) AS week, 
            theme_1, 
            COUNT(*) AS total 
        FROM {table_name}
        GROUP BY week, theme_1
        ORDER BY week ASC
    '''
    return pd.read_sql(query, con=engine)
