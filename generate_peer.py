import sqlite3
import pandas as pd

conn = sqlite3.connect("db/n100.db")

financial = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

try:
    peer = pd.read_sql(
        "SELECT * FROM peer_groups",
        conn
    )
except:
    peer = pd.DataFrame()

conn.close()

writer = pd.ExcelWriter(
    "output/peer_comparison.xlsx",
    engine="openpyxl"
)

if peer.empty:

    financial.to_excel(
        writer,
        sheet_name="All Companies",
        index=False
    )

else:

    peer_column = peer.columns[1]

    for group in peer[peer_column].dropna().unique():

        companies = peer[
            peer[peer_column] == group
        ]

        company_col = peer.columns[0]

        report = financial[
            financial["company_id"].isin(
                companies[company_col]
            )
        ]

        report.to_excel(
            writer,
            sheet_name=str(group)[:31],
            index=False
        )

writer.close()

print("peer_comparison.xlsx created successfully.")