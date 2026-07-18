import sqlite3
import pandas as pd
from pathlib import Path

db_path = "db/n100.db"

conn = sqlite3.connect(db_path)

try:
    df = pd.read_sql("SELECT company_id, year, cash_from_operations_cr FROM financial_ratios", conn)
except Exception:
    print("financial_ratios table not found.")
    conn.close()
    exit()

conn.close()

df["cfo_sign"] = df["cash_from_operations_cr"].apply(lambda x: "+" if x >= 0 else "-")

# Placeholder values (until full CFI/CFF data is integrated)
df["cfi_sign"] = "-"
df["cff_sign"] = "-"

def classify(cfo, cfi, cff):
    signs = (cfo, cfi, cff)

    if signs == ("+", "-", "-"):
        return "Reinvestor"
    elif signs == ("+", "+", "-"):
        return "Liquidating Assets"
    elif signs == ("-", "+", "+"):
        return "Distress Signal"
    elif signs == ("-", "-", "+"):
        return "Growth Funded by Debt"
    elif signs == ("+", "+", "+"):
        return "Cash Accumulator"
    elif signs == ("-", "-", "-"):
        return "Pre-Revenue"
    elif signs == ("+", "-", "+"):
        return "Mixed"
    else:
        return "Other"

df["pattern_label"] = df.apply(
    lambda r: classify(r["cfo_sign"], r["cfi_sign"], r["cff_sign"]),
    axis=1,
)

output_path = Path("output") / "capital_allocation.csv"

df[
    [
        "company_id",
        "year",
        "cfo_sign",
        "cfi_sign",
        "cff_sign",
        "pattern_label",
    ]
].to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")