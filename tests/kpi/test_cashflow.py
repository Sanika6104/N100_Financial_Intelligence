import pandas as pd
from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality,
    capex_intensity,
    capital_allocation_pattern,
)


def test_free_cash_flow():
    assert free_cash_flow(1000, 300) == 700


def test_cfo_quality():
    assert cfo_quality(500, 250) == 2


def test_cfo_quality_zero():
    assert cfo_quality(100, 0) is None


def test_capex_intensity():
    assert capex_intensity(100, 1000) == 0.1


def test_capex_intensity_zero():
    assert capex_intensity(100, 0) is None


def test_capital_allocation_pattern(tmp_path):
    df = pd.DataFrame({
        "Company": ["ABC"],
        "FCF": [700]
    })

    output = tmp_path / "capital_allocation.csv"

    result = capital_allocation_pattern(df, output)

    assert output.exists()
    assert str(output) == result