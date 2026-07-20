import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("reports/radar_charts", exist_ok=True)

conn = sqlite3.connect("db/n100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

conn.close()

metrics = [
    "return_on_equity_pct",
    "net_profit_margin_pct",
    "asset_turnover",
    "debt_to_equity"
]

labels = [
    "ROE",
    "NPM",
    "Asset Turnover",
    "Debt/Equity"
]

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))

latest = (
    df.sort_values("year")
      .groupby("company_id")
      .tail(1)
)

count = 0

for _, company in latest.iterrows():

    values = []

    for metric in metrics:
        value = company.get(metric, 0)

        if pd.isna(value):
            value = 0

        values.append(value)

    values.append(values[0])

    fig = plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(company["company_id"])

    plt.savefig(
        f"reports/radar_charts/{company['company_id']}_radar.png"
    )

    plt.close()

    count += 1

print(f"Generated {count} radar charts.")