def calculate_cagr(beginning_value, ending_value, years):
    """
    Generic CAGR Formula
    Returns only CAGR value (keeps existing tests compatible)
    """

    if beginning_value <= 0 or ending_value <= 0 or years <= 0:
        return None

    return ((ending_value / beginning_value) ** (1 / years) - 1) * 100


def revenue_cagr(start_revenue, end_revenue, years):
    return calculate_cagr(start_revenue, end_revenue, years)


def pat_cagr(start_pat, end_pat, years):
    return calculate_cagr(start_pat, end_pat, years)


def eps_cagr(start_eps, end_eps, years):
    return calculate_cagr(start_eps, end_eps, years)


# ---------------- Sprint 2 Edge Case Handler ---------------- #

def calculate_cagr_with_flag(beginning_value, ending_value, years):
    """
    Returns:
    (cagr_value, flag)

    Flags:
    None
    TURNAROUND
    DECLINE_TO_LOSS
    BOTH_NEGATIVE
    ZERO_BASE
    INSUFFICIENT
    """

    if years <= 0:
        return None, "INSUFFICIENT"

    if beginning_value == 0:
        return None, "ZERO_BASE"

    if beginning_value > 0 and ending_value < 0:
        return None, "DECLINE_TO_LOSS"

    if beginning_value < 0 and ending_value > 0:
        return None, "TURNAROUND"

    if beginning_value < 0 and ending_value < 0:
        return None, "BOTH_NEGATIVE"

    if beginning_value <= 0 or ending_value <= 0:
        return None, "INSUFFICIENT"

    cagr = ((ending_value / beginning_value) ** (1 / years) - 1) * 100

    return cagr, None