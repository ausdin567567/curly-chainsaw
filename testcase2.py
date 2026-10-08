"""
Unit test for issue #2: filter_transactions(transactions, start_date, end_date, categories).
"""
from datetime import date

from app.filters import filter_transactions


def test_transaction_on_end_date_is_included():
    transactions = [
        {"id": 1, "date": date(2026, 1, 31), "category": "Dining"},
        {"id": 2, "date": date(2026, 2, 1), "category": "Dining"},
    ]

    result = filter_transactions(
        transactions,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 1, 31),
        categories=["Dining"],
    )

    assert [t["id"] for t in result] == [1]