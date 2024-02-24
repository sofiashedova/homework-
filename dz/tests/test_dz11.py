import pytest   
from dz11.dz_2v import Date   
 
 

import pytest

class TestDate:
    @pytest.mark.parametrize("year, month, day, expected", [
        (2022, 12, 31, True),  # Valid date
        (2023, 2, 29, False),   # Invalid date
        # Добавьте другие тестовые случаи здесь
    ])
    def test_validate(self, year, month, day, expected):
        date = Date(year, month, day)
        assert date.validate() == expected

    @pytest.mark.parametrize("year, month, day", [
        (2022, 12, 31),
        (2023, 2, 28),
        # Добавьте другие тестовые случаи здесь
    ])
    def test_str(self, year, month, day):
        date = Date(year, month, day)
        assert date.str() == f"{year}.{month}.{day}"

    @pytest.mark.parametrize("year, month, day", [
        (2022, 12, 31),
        (2023, 2, 28),
        # Добавьте другие тестовые случаи здесь
    ])
    def test_input_date(self, year, month, day):
        date = Date()
        date.input_date(f"{year}.{month}.{day}")
        assert (date.year, date.month, date.day) == (year, month, day)


