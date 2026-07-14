def debt_to_equity(total_debt, equity):
    """
    Debt to Equity Ratio = Total Debt / Equity
    """
    if equity <= 0:
        return None
    return total_debt / equity


def interest_coverage(ebit, interest_expense):
    """
    Interest Coverage = EBIT / Interest Expense
    """
    if interest_expense == 0:
        return None
    return ebit / interest_expense


def asset_turnover(revenue, total_assets):
    """
    Asset Turnover = Revenue / Total Assets
    """
    if total_assets == 0:
        return None
    return revenue / total_assets


def net_debt(total_debt, cash):
    """
    Net Debt = Total Debt - Cash
    """
    return total_debt - cash