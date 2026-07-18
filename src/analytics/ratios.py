import logging

# Configure logging
logging.basicConfig(
    filename="output/ratio_edge_cases.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin = (Net Profit / Sales) * 100
    """
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin = (Operating Profit / Sales) * 100
    """
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def check_opm_difference(calculated_opm, source_opm, company="Unknown", year="Unknown"):
    """
    Log if calculated OPM differs from source by more than 1%
    """
    if calculated_opm is None or source_opm is None:
        return

    if abs(calculated_opm - source_opm) > 1:
        logging.info(
            f"OPM mismatch | Company={company} | Year={year} | "
            f"Calculated={calculated_opm:.2f} | Source={source_opm:.2f}"
        )


def return_on_equity(net_profit, equity, reserves):
    """
    ROE = Net Profit / (Equity + Reserves) * 100
    """
    capital = equity + reserves

    if capital <= 0:
        return None

    return (net_profit / capital) * 100


def return_on_capital_employed(
    ebit,
    equity,
    reserves,
    borrowings,
    sector=None
):
    """
    ROCE = EBIT / (Equity + Reserves + Borrowings) * 100
    """

    capital = equity + reserves + borrowings

    if capital <= 0:
        return None

    roce = (ebit / capital) * 100

    # Financial companies use sector-relative benchmark
    if sector == "Financials":
        return roce

    return roce


def return_on_assets(net_profit, total_assets):
    """
    ROA = Net Profit / Total Assets * 100
    """
    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100