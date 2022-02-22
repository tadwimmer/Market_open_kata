import datetime

from src.market_open import is_market_open


def test_is_market_open():
    assert is_market_open(datetime.datetime(2022,2,22))

def test_is_market_open_saturday():
    # New Years not observed by NYSE if it falls on a Saturday
    assert not is_market_open(datetime.datetime(2022, 1, 1))

def test_is_market_open_sunday():
    assert not is_market_open(datetime.datetime(2022, 2, 20))

def test_is_market_open_new_years():
    assert not is_market_open(datetime.datetime(2024, 1, 1))

def test_is_market_open_new_years_monday_obs():
    assert not is_market_open(datetime.datetime(2023, 1, 2))

def test_civil_rights_day_2022():
    assert not is_market_open(datetime.datetime(2022, 1, 17))

def test_presidents_day_2022():
    assert not is_market_open(datetime.datetime(2022, 2, 21))