import pytest
import price_info


# ---------- total_cost_shopping() ----------
def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    assert result == pytest.approx(46.75)


# ---------- cost_of_fruits() ----------
def test_cost_of_fruits_apple():
    result = price_info.cost_of_fruits('apple', 10)
    assert result == pytest.approx(12.00)

def test_cost_of_fruits_watermelon():
    result = price_info.cost_of_fruits('watermelon', 1)
    assert result == pytest.approx(6.50)

def test_cost_of_fruits_zero_quantity():
    result = price_info.cost_of_fruits('pear', 0)
    assert result == 0