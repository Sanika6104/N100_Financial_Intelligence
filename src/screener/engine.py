import sqlite3
import pandas as pd
import yaml

DB_PATH = "db/n100.db"
CONFIG_PATH = "config/screener_config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)


def load_financial_ratios():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        "SELECT * FROM financial_ratios",
        conn
    )

    conn.close()
    return df


def apply_filters(df, config):
    """
    Apply threshold filters to financial_ratios DataFrame.
    """

    if "return_on_equity_pct" in df.columns:
        df = df[df["return_on_equity_pct"] >= config["roe_min"]]

    if "debt_to_equity" in df.columns:
        df = df[df["debt_to_equity"] <= config["de_max"]]

    if "free_cash_flow_cr" in df.columns:
        df = df[df["free_cash_flow_cr"] >= config["fcf_min"]]

    if "operating_profit_margin_pct" in df.columns:
        df = df[df["operating_profit_margin_pct"] >= config["opm_min"]]

    if "asset_turnover" in df.columns:
        df = df[df["asset_turnover"] >= config["asset_turnover_min"]]

    return df


def main():
    config = load_config()

    df = load_financial_ratios()

    print(f"Original rows: {len(df)}")

    filtered = apply_filters(df, config)

    print(f"Filtered rows: {len(filtered)}")

    print(filtered.head())


if __name__ == "__main__":
    main()