from src.screener.engine import apply_filters


def quality_compounder(df, config):
    config["roe_min"] = 15
    config["de_max"] = 1
    config["fcf_min"] = 0
    return apply_filters(df, config)


def value_pick(df, config):
    config["de_max"] = 2
    return apply_filters(df, config)


def growth_accelerator(df, config):
    config["roe_min"] = 20
    return apply_filters(df, config)


def dividend_champion(df, config):
    config["fcf_min"] = 0
    return apply_filters(df, config)


def debt_free_bluechip(df, config):
    df = df[df["debt_to_equity"] == 0]
    return df


def turnaround_watch(df, config):
    df = df[df["free_cash_flow_cr"] > 0]
    return df