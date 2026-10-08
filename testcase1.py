"""
Unit test for issue #1: validate_date_range(start_date, end_date).

"""
from datetime import date

import pytest

from app.filters import validate_date_range


def test_valid_range_returns_parsed_dates():
    assert validate_date_range("2026-01-01", "2026-01-31") == (date(2026, 1, 1), date(2026, 1, 31))


def test_start_after_end_raises():
    with pytest.raises(ValueError):
        validate_date_range("2026-02-01", "2026-01-01")