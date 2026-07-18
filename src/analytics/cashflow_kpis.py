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


def cfo_quality_score(cfo_pat_ratio):
    """
    CFO Quality Score
    """

    if cfo_pat_ratio is None:
        return None

    if cfo_pat_ratio > 1:
        return "High Quality"

    elif cfo_pat_ratio >= 0.5:
        return "Moderate"

    else:
        return "Accrual Risk"


def capex_intensity(capex, revenue):
    """
    CapEx Intensity
    """

    if revenue == 0:
        return None

    return abs(capex) / revenue


def capex_category(intensity):
    """
    CapEx Category
    """

    if intensity is None:
        return None

    if intensity < 3:
        return "Asset Light"

    elif intensity <= 8:
        return "Moderate"

    return "Capital Intensive"


def fcf_conversion_rate(fcf, operating_profit):
    """
    FCF Conversion Rate
    """

    if operating_profit == 0:
        return None

    return (fcf / operating_profit) * 100


def classify_capital_allocation(cfo, cfi, cff, cfo_pat_ratio=None):
    """
    Capital Allocation Pattern
    """

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    if signs == ("+", "-", "-"):
        if cfo_pat_ratio is not None and cfo_pat_ratio > 1:
            return "Shareholder Returns"
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

    return "Other"


def capital_allocation_pattern(df, output_file="output/capital_allocation.csv"):
    """
    Save Capital Allocation CSV
    """

    df.to_csv(output_file, index=False)

    return str(output_file)