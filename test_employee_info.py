import pytest
import employee_info


# ---------- get_employees_by_age_range() ----------
def test_age_range_normal():
    result = employee_info.get_employees_by_age_range(25, 35)
    names = [e["name"] for e in result]
    assert names == ["John", "Mike"]

def test_age_range_all():
    result = employee_info.get_employees_by_age_range(20, 50)
    assert len(result) == 6

def test_age_range_none():
    result = employee_info.get_employees_by_age_range(50, 60)
    assert result == []


# ---------- calculate_average_salary() ----------
def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert result == pytest.approx(60166.67, abs=0.01)


# ---------- get_employees_by_dept() ----------
def test_dept_marketing():
    result = employee_info.get_employees_by_dept("Marketing")
    names = [e["name"] for e in result]
    assert names == ["Jane", "Mary"]

def test_dept_engineering():
    result = employee_info.get_employees_by_dept("Engineering")
    names = [e["name"] for e in result]
    assert names == ["Chloe", "Mike"]

def test_dept_not_found():
    result = employee_info.get_employees_by_dept("HR")
    assert result == []