from datetime import datetime
import sys

import pytest
from mailroom import Donor, DonorCollection

datetime_pattern = "%Y-%m-%d %H:%M:%S.%f"

now = datetime.now()

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

    donor = Donor('Bill Murray', [{'amount': 20.00, 'date': now}, {'amount': 30.00, 'date': now}, {'amount': 40.00, 'date': now}])
    assert donor.average_donation == 30.00


def test_Donor_total_donation():

    donor = Donor('Bill Murray', [{'amount': 20.00, 'date': now}, {'amount': 30.00, 'date': now}, {'amount': 40.00, 'date': now}])
    assert donor.total_donation == 90.00


def test_Donor_ordering():
    bill = Donor('Bill Murray', [{'amount': 500.00, 'date': now}])
    ted = Donor('Ted Bogus', [{'amount': 50.00, 'date': now}])
    assert bill != ted
    assert ted < bill

def test_most_recent_donation():
    a = datetime(2019, 12, 2, 23, 29, 17, 120741)
    b = datetime(2019, 12, 2, 23, 28, 25, 610351)
    c = datetime(2019, 12, 2, 23, 28, 29, 310351)
    donor = Donor('Bill Murray', [{'amount': 20.00, 'date': a}, {'amount': 30.00, 'date': b}, {'amount': 40.00, 'date': c}])
    assert donor.`most_recent_donation() == (20.00, a)


def test_DonorCollection_add_donor():
    donors = DonorCollection()
    bill = Donor('Bill Murray', [{'amount': 600.32, 'date': now}])
    donors.add_donor(bill)
    assert bill in donors


def test_DonorCollection_from_dict():

    d = DonorCollection.from_dict({'Bill Murray': [{'amount': 500.00, 'date': now}]})

    assert isinstance(d, DonorCollection)

