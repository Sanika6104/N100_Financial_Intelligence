def debt_to_equity(borrowings, equity, reserves=0, sector=None):
    """
    Debt to Equity = Borrowings / (Equity + Reserves)

    Compatible with existing tests.
    """

    if borrowings == 0:
        return 0

    capital = equity + reserves

    if capital <= 0:
        return None

    ratio = borrowings / capital

    # Optional Sprint-2 flag
    if sector != "Financials" and ratio > 5:
        pass

    return ratio


def interest_coverage(operating_profit, interest, other_income=0):
    """
    Interest Coverage Ratio

    Compatible with existing tests.
    """

    if interest == 0:
        return None

    return (operating_profit + other_income) / interest


def net_debt(borrowings, investments):
    """
    Net Debt
    """
    return borrowings - investments


def asset_turnover(sales, total_assets):
    """
    Asset Turnover
    """

    if total_assets == 0:
        return None

    return sales / total_assets


# ---------- Optional helper functions for Sprint 2 ----------

def high_leverage_flag(de_ratio, sector=None):
    """
    Returns True if D/E > 5 for non-financial companies.
    """
    if de_ratio is None:
        return False

    if sector == "Financials":
        return False

    return de_ratio > 5


def icr_label(interest):
    """
    Debt Free label.
    """
    if interest == 0:
        return "Debt Free"
    return ""


def icr_warning(icr):
    """
    Warning if Interest Coverage < 1.5
    """
    if icr is None:
        return False

    return icr < 1.5