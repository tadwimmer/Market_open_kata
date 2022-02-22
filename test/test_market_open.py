import datetime

from src.market_open import is_market_open


def test_is_market_open_02222022():
    assert is_market_open(datetime.datetime(2022, 2, 22))

def test_is_market_open_saturday():
    # New Years not observed by NYSE if it falls on a Saturday
    assert not is_market_open(datetime.datetime(2022, 1, 1))

def test_is_market_open_sunday():
    assert not is_market_open(datetime.datetime(2022, 2, 20))

def test_is_market_open_sunday_():
    assert not is_market_open(datetime.datetime(2022, 2, 26))

def test_is_market_open_new_years():
    assert not is_market_open(datetime.datetime(2024, 1, 1))

def test_is_market_open_new_years_monday_obs():
    assert not is_market_open(datetime.datetime(2023, 1, 2))

def test_civil_rights_day_2022():
    assert not is_market_open(datetime.datetime(2022, 1, 17))

def test_civil_rights_day_2023():
    assert not is_market_open(datetime.datetime(2023, 1, 16))

def test_presidents_day_2022():
    assert not is_market_open(datetime.datetime(2022, 2, 21))

def test_presidents_day_2023():
    assert not is_market_open(datetime.datetime(2023, 2, 20))

def test_memorial_day_2022():
    assert not is_market_open(datetime.datetime(2022, 5, 30))

def test_memorial_day_2023():
    assert not is_market_open(datetime.datetime(2023, 5, 29))

def test_labor_day_2022():
    assert not is_market_open(datetime.datetime(2022,9, 5))

def test_juneteenth_2023():
    assert not is_market_open(datetime.datetime(2023,6, 19))

def test_juneteenth_2022_monday_observance():
    assert not is_market_open(datetime.datetime(2022,6, 20))

def test_independence_day():
    assert not is_market_open(datetime.datetime(2022, 7,4))

def test_thanksgiving():
    assert not is_market_open(datetime.datetime(2022, 11, 24))

def test_christmas_2023():
    assert not is_market_open(datetime.datetime(2023, 12, 25))

def test_christmas_2022_monday_observance():
    assert not is_market_open(datetime.datetime(2022, 12, 26))

def test_christmas_2021_friday_observance():
    assert not is_market_open(datetime.datetime(2021, 12, 24))

def test_new_years_eve_2021():
    assert is_market_open(datetime.datetime(2021, 12,31))