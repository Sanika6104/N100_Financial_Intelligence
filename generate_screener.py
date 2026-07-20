import sqlite3
import pandas as pd

from src.screener.engine import load_config
from src.screener.presets import (
    quality_compounder,
    value_pick,
    growth_accelerator,
    dividend_champion,
    debt_free_bluechip,
    turnaround_watch,
)
from src.screener.scoring import composite_score

conn = sqlite3.connect("db/n100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

config = load_config()

presets = {
    "Quality Compounder": quality_compounder(df.copy(), config.copy()),
    "Value Pick": value_pick(df.copy(), config.copy()),
    "Growth Accelerator": growth_accelerator(df.copy(), config.copy()),
    "Dividend Champion": dividend_champion(df.copy(), config.copy()),
    "Debt Free Bluechip": debt_free_bluechip(df.copy(), config.copy()),
    "Turnaround Watch": turnaround_watch(df.copy(), config.copy()),
}

writer = pd.ExcelWriter(
    "output/screener_output.xlsx",
    engine="openpyxl"
)

for name, data in presets.items():
    data = composite_score(data)
    data.to_excel(writer, sheet_name=name[:31], index=False)

writer.close()

conn.close()

print("Excel file created successfully.")