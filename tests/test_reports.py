import pytest
from reports import Reports
from create_database import Database


def test_most_popular_item():
    db = Database("test.db")

    report = Reports(db)

    assert report.most_popular_item()['product_name'][0] == ' ramen'


def test_member_ranking_details():
    db = Database("test.db")

    report = Reports(db)

    assert len(report.member_ranking_details()) == 15

