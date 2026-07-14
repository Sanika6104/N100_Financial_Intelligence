from src.analytics.cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr,
)


def test_revenue_cagr():
    result = revenue_cagr(100, 200, 5)
    assert round(result, 2) == 14.87


def test_pat_cagr():
    result = pat_cagr(50, 100, 5)
    assert round(result, 2) == 14.87


def test_eps_cagr():
    result = eps_cagr(10, 20, 5)
    assert round(result, 2) == 14.87


def test_zero_beginning():
    assert revenue_cagr(0, 100, 5) is None


def test_negative_values():
    assert pat_cagr(-10, 100, 5) is None


def test_zero_years():
    assert eps_cagr(10, 20, 0) is None