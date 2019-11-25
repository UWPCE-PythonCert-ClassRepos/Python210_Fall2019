from mailroom import Donor
from datetime import datetime
import pytest

test_donors = {"William Gates": [{"amount": 653784.49, "date": "11-08-2019"}], "Mark Zuckerberg": [{"amount": 1600.1, "date": "08-12-2018"}, {"amount": 300.34, "date": "08-12-2019"}], "Jeff Bezos": [{"amount": 877.33, "date": "11-22-2019"}], "Paul Allen": [{"amount": 405, "date": "01-01-2017"}, {"amount": 678.23, "date": "01-01-2019"}, {"amount": 200.12, "date": "01-01-2018"}], "Jay Ferguson": [{"amount": 21.12, "date": "11-21-2019"}]}


def test_Donor_1():
    with pytest.raises(TypeError):
        assert Donor(5)

def test_Donor_2():
    with pytest.raises(TypeError):
        assert Donor('Bill Murray', [{'amount':55.00, 'date': '11-29-2019'}])

def test_Donor_3():
    donor = Donor(' bIll MuRray   ', [{'amount': 55.21, 'date': datetime.now()}])
    assert donor.name == 'Bill Murray'

def test_Donor_add_donation():
    donor = Donor('Bill Murray', [{'amount': 23.20, 'date': datetime.now()}])
    donor.add_donation(44.13)
    assert len(donor.donations) == 2

def test_Donor_average_donation():
    now = datetime.now()
    donor = Donor('Bill Murray', [{'amount': 20.00, 'date': now}, {'amount': 30.00, 'date': now}, {'amount': 40.00, 'date': now}])
    assert donor.average_donation() == 30.00

