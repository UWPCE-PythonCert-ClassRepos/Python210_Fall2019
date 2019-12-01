from datetime import datetime
import sys

import pytest
from mailroom import Donor, Donors

datetime_pattern = "%Y-%m-%d %H:%M:%S.%f"
test_donors = {"William Gates": [{"amount": 653784.49, "date": datetime.strptime("2019-10-15 13:32:06.497528", datetime_pattern)}], "Mark Zuckerberg": [{"amount": 1600.1, "date": datetime.strptime("2018-10-15 13:32:06.497528", datetime_pattern)}, {"amount": 300.34, "date": datetime.strptime("2019-01-15 09:33:06.123528", datetime_pattern)}], "Jeff Bezos": [{"amount": 877.33, "date": datetime.strptime("2019-11-22 10:32:06.497528", datetime_pattern)}], "Paul Allen": [{"amount": 405, "date": datetime.strptime("2017-10-15 11:32:06.497528", datetime_pattern)}, {"amount": 678.23, "date": datetime.strptime("2019-01-01 13:32:06.497528", datetime_pattern)}, {"amount": 200.12, "date": datetime.strptime("2018-01-01 13:32:06.497528", datetime_pattern)}], "Jay Ferguson": [{"amount": 21.12, "date": datetime.strptime("2019-01-01 12:32:06.497528", datetime_pattern)}], "Bill Murray": [{"amount": 500.0, "date": datetime.strptime("2019-11-25 17:33:56.497528", datetime_pattern)}]}

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

def test_Donors():
    donors = Donors('test_donors.json')
    for i in donors.donors.values():
        assert isinstance(i[0]['date'], datetime)

def test_Donors_add_donor():
    donors = Donors('test_donors.json')
    now = datetime.now()
    bill = Donor('Bill Murray', [{'amount': 600.32, 'date': now}])
    donors.add_donor(bill)
    assert donors.donors['Bill Murray'][0] == {'amount': 600.32, 'date': now}
