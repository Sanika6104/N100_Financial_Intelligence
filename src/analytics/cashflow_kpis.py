import pandas as pd


def free_cash_flow(cfo, capex):
    """
    Free Cash Flow = CFO - CapEx
    """
    return cfo - capex


def cfo_quality(cfo, net_profit):
    """
    CFO Quality = CFO / Net Profit
    """
    if net_profit == 0:
        return None
    return cfo / net_profit


def capex_intensity(capex, revenue):
    """
    CapEx Intensity = CapEx / Revenue
    """
    if revenue == 0:
        return None
    return capex / revenue


def capital_allocation_pattern(df, output_file="output/capital_allocation.csv"):
    """
    Save capital allocation summary to CSV.
    """
    df.to_csv(output_file, index=False)
    return str(output_file)