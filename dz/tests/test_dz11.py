import pytest   
from dz11.dz_2v import Date   
 
 

class TestDate:
    @pytest.mark.parametrize("year, month, day", [
        (2022, 12, 31),
        (2000, 2, 29),
        (1900, 2, 28),
        (2023, 10, 15),
        (2024, 1, 31)
    ])
    def test_init(self, year, month, day):
        date = Date(year, month, day)
        assert date.year == year
        assert date.month == month
        assert date.day == day

class Date:
    def __init__(self, year=1, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

class TestInputDate:
    @pytest.mark.parametrize("user_input, expected_year, expected_month, expected_day", [
        ("2022.12.31", 2022, 12, 31),
        ("2000.02.29", 2000, 2, 29),
        ("1900.02.28", 1900, 2, 28),
        ("2023.10.15", 2023, 10, 15),
        ("2024.01.31", 2024, 1, 31)
    ])
    def test_input_date(self, monkeypatch, user_input, expected_year, expected_month, expected_day):
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        date_obj = Date()
        date_obj.input_date()
        assert date_obj.year == expected_year
        assert date_obj.month == expected_month
        assert date_obj.day == expected_day

class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def input_date(self):
        year, month, day = map(int, input("Введите дату ГГГГ.ММ.ДД: ").split('.'))
        self.year = year
        self.month = month
        self.day = day

class TestDateStr:
    @pytest.mark.parametrize("year, month, day, expected_output", [
        (2022, 12, 31, "2022.12.31"),
        (2000, 2, 29, "2000.2.29"),
        (1900, 2, 28, "1900.2.28"),
        (2023, 10, 15, "2023.10.15"),
        (2024, 1, 31, "2024.1.31")
    ])
    def test_date_str(self, year, month, day, expected_output):
        date = Date(year, month, day)
        assert str(date) == expected_output

class Date:
    def __init__(self, year=1, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}.{self.month}.{self.day}"

    @pytest.mark.parametrize("year, month, day, expected_result", [
        (2022, 12, 31, True),   # Valid date
        (2000, 2, 29, True),    # Leap year
        (1900, 2, 29, False),   # Not a leap year
        (2023, 10, 15, True),   # Valid date
        (2024, 1, 31, True)     # Valid date
    ])
    def test_date_validation(self, year, month, day, expected_result):
        date_obj = Date(year, month, day)
        assert date_obj.validate() == expected_result

