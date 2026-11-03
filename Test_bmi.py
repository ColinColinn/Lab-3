import ET0735_Lab2.bmi as bmi


def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.7, 60) == 0    # BMI 20.8
    assert bmi.calculate_bmi(2.0, 74) == 0    # BMI 18.5, lower boundary


def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.7, 80) == 1    # BMI 27.7
    assert bmi.calculate_bmi(2.0, 100) == 1   # BMI 25.0, boundary


def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.7, 50) == -1   # BMI 17.3
    assert bmi.calculate_bmi(2.0, 73) == -1   # BMI 18.25, just under