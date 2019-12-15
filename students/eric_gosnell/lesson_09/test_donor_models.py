"""
Eric Gosnell
Lesson 9 - Object Oriented Mailroom
12.10.2019

        ****    Pytest Module  ****
"""

from donor_models import *

# ----------     Test Donor class     ----------- #


def test_new_donor_and_name():
    a_donor = Donor("A Donor")
    h_donor = Donor("h donor")
    assert a_donor.name == "A Donor"
    assert h_donor.name == "H Donor"  # test capitalization


def test_add_donation():
    b_donor = Donor("B Donor")
    b_donor.add_donation("12/01/2019", 4000.00)
    assert b_donor.recent_donation == 4000.00


def test_donation_list():
    c_donor = Donor("C Donor")
    c_donor.add_donation("12/01/2019", 100.00)
    c_donor.add_donation("12/02/2019", 200)
    c_donor.add_donation("12/03/2019", 300.0)
    assert c_donor.donations == [{'12/01/2019': 100.0},
                                 {'12/02/2019': 200.0},
                                 {'12/03/2019': 300.0}]


def test_recent_donation():
    d_donor = Donor("D Donor")
    d_donor.add_donation("12/01/2019", 1000.00)
    d_donor.add_donation("12/02/2019", 2000)
    d_donor.add_donation("12/03/2019", 3000.0)
    assert d_donor.recent_donation == 3000.0


def test_recent_date():
    e_donor = Donor("D Donor")
    e_donor.add_donation("12/01/2019", 10.00)
    e_donor.add_donation("12/02/2019", 20)
    e_donor.add_donation("12/03/2019", 30.0)
    assert e_donor.recent_date == "12/03/2019"


def test_sum_donations():
    f_donor = Donor("F Donor")
    f_donor.add_donation("12/01/2019", 100)
    f_donor.add_donation("12/02/2019", 200)
    f_donor.add_donation("12/03/2019", 300)
    assert f_donor.sum_donations == 600


def test_qty_donations():
    g_donor = Donor("G Donor")
    g_donor.add_donation("12/01/2019", 100)
    g_donor.add_donation("12/02/2019", 200)
    g_donor.add_donation("12/03/2019", 300)
    assert g_donor.qty_donations == 3


def test_avg_donation():
    i_donor = Donor("I Donor")
    i_donor.add_donation("12/01/2019", 100)
    i_donor.add_donation("12/02/2019", 200)
    i_donor.add_donation("12/03/2019", 300)
    assert i_donor.avg_donation == 200

# ----------     Test Charity class     ----------- #


def test_charity_donor_list():
    j_donor = Donor("J Donor")
    k_donor = Donor("K Donor")
    l_donor = Donor("L Donor")

    a_charity = Charity("A Charity")

    a_charity.add_donor(j_donor)
    a_charity.add_donor(k_donor)
    a_charity.add_donor(l_donor)

    assert a_charity.donor_list == [Donor("J Donor"),
                                    Donor("K Donor"),
                                    Donor("L Donor")]


def sort_key(donor):
    return donor.sum_donations


def test_sorted_donors():
    m_donor = Donor("M Donor")
    n_donor = Donor("N Donor")
    o_donor = Donor("O Donor")

    m_donor.add_donation("12/01/2019", 100)
    m_donor.add_donation("12/02/2019", 200)
    n_donor.add_donation("12/01/2019", 300)
    n_donor.add_donation("12/02/2019", 400)
    o_donor.add_donation("12/01/2019", 500)
    o_donor.add_donation("12/02/2019", 600)

    b_charity = Charity("B Charity")

    b_charity.add_donor(m_donor)
    b_charity.add_donor(n_donor)
    b_charity.add_donor(o_donor)

    donor_list = sorted(b_charity.donor_list, key=sort_key, reverse=False)
    assert donor_list[0] == m_donor

    donor_list = sorted(b_charity.donor_list, key=sort_key, reverse=True)
    assert donor_list[0] == o_donor
