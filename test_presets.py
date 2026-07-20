import sqlite3
import pandas as pd

from src.screener.engine import load_config
from src.screener.presets import quality_compounder
from src.screener.scoring import composite_score

conn = sqlite3.connect("db/n100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

config = load_config()

result = quality_compounder(df, config)

result = composite_score(result)

print(
    result[
        [
            "company_id",
            "year",
            "return_on_equity_pct",
            "debt_to_equity",
            "composite_quality_score",
        ]
    ].head(10)
)

print()

print("Companies:", len(result))

conn.close()