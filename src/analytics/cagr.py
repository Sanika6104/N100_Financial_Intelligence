import math


def calculate_cagr(beginning_value, ending_value, years):
    """
    Generic CAGR Formula
    CAGR = ((Ending / Beginning) ** (1 / Years) - 1) * 100
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