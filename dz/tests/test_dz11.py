import pytest   
from dz11.dz_2v import Date   
 
 

@pytest.mark.parametrize("input_data, expected_output", [
    ("2022.10.15", "2022.10.15"),
    ("2000.1.1", "2000.1.1"),
    ("1999.12.31", "1999.12.31"),
    ("2023.5.20", "2023.5.20"),
    ("1980.11.25", "1980.11.25"),
    ("1975.7.4", "1975.7.4"),
    ("1658.1.17", "1658.1.17")
])
def test_input_date(monkeypatch, input_data, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: input_data)
    date = Date()
    date.input_date()
    assert str(date) == expected_output

@pytest.mark.parametrize("year, month, day, expected_exception", [
    (2022, 2, 29, ValueError),
    (2021, 2, 28, None),
    (2000, 2, 29, None),
    (1999, 4, 31, ValueError),
])
def test_valid_date(year, month, day, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            Date(year, month, day)
    else:
        date = Date(year, month, day)
        assert date.year == year
        assert date.month == month
        assert date.day == day

@pytest.mark.parametrize("year, month, day, expected_exception", [
    (2022, 2, 29, ValueError),
    (2021, 2, 28, None),
    (2000, 2, 29, None),
    (1999, 4, 31, ValueError),
])
def test_invalid_date(year, month, day, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            Date(year, month, day)
    else:
        date = Date(year, month, day)
        assert date.year == year
        assert date.month == month
        assert date.day == day


@pytest.mark.parametrize("year, month, day, expected_output", 
                         [ 
                             (2022, 10, 15, "2022.10.15"), 
                             (2000, 1, 1, "2000.1.1"), 
                             (1999, 12, 31, "1999.12.31"),
                             (2023, 5, 20, "2023.5.20"),
                             (1980, 11, 25, "1980.11.25"),
                             (1975, 7, 4, "1975.7.4")
                         ]) 
def test_str_method(year, month, day, expected_output): 
    date_obj = Date(year, month, day) 
    assert str(date_obj) == expected_output


@pytest.mark.parametrize("year, month, day, expected_output", [
    (2021, 2, 28, True),
    (2020, 2, 29, True),
    (2020, 12, 31, True)
])
def test_validate(year, month, day, expected_output):
    instance = Date(year, month, day)
    assert instance.validate() == expected_output

