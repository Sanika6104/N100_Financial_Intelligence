import pandas as pd


def composite_score(df):
    """
    Compute a simple composite quality score.
    """

    score = (
        df["return_on_equity_pct"].fillna(0) * 0.35
        + df["net_profit_margin_pct"].fillna(0) * 0.25
        + df["asset_turnover"].fillna(0) * 20
        + (1 - df["debt_to_equity"].fillna(0)) * 20
    )

    df["composite_quality_score"] = score

    return df.sort_values(
        "composite_quality_score",
        ascending=False
    )