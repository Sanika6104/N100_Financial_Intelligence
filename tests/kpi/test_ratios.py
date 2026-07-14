from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
)


def test_net_profit_margin():
    assert net_profit_margin(100, 1000) == 10


def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(150, 1000) == 15


def test_return_on_equity():
    assert round(return_on_equity(100, 400, 100), 2) == 20.00


def test_return_on_equity_negative():
    assert return_on_equity(100, -500, 100) is None


def test_return_on_capital_employed():
    assert round(return_on_capital_employed(120, 400, 100, 100), 2) == 20.00


def test_return_on_assets():
    assert return_on_assets(100, 1000) == 10


def test_return_on_assets_zero():
    assert return_on_assets(100, 0) is None