import sqlite3
import pandas as pd


DB = "db/n100.db"


def load_tables():
    conn = sqlite3.connect(DB)

    financial = pd.read_sql(
        "SELECT * FROM financial_ratios",
        conn
    )

    companies = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    return financial, companies


def calculate_percentile(df, metric):

    df = df.copy()

    df["percentile_rank"] = (
        df[metric]
        .rank(method="average", pct=True)
        * 100
    )

    return df