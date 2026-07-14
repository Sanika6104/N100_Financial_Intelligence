from src.analytics.leverage import (
    debt_to_equity,
    interest_coverage,
    asset_turnover,
    net_debt,
)


def test_debt_to_equity():
    assert debt_to_equity(200, 100) == 2


def test_debt_to_equity_zero():
    assert debt_to_equity(100, 0) is None


def test_interest_coverage():
    assert interest_coverage(500, 100) == 5


def test_interest_coverage_zero():
    assert interest_coverage(500, 0) is None


def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2


def test_asset_turnover_zero():
    assert asset_turnover(1000, 0) is None


def test_net_debt():
    assert net_debt(500, 100) == 400