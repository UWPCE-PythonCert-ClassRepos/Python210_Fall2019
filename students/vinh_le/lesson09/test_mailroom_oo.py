import pytest
import datetime
import os
from donor import Donation, Donor, Charity


# Test Donation Class
def test_donation_attributes():
    donation_1 = Donation(100)
    curr_date = datetime.datetime.now()
    assert donation_1.amount == 100
    assert donation_1.date == curr_date
    assert donation_1.formatted_date() == curr_date.strftime("%m-%d-%y")


# Test Donor Class
def test_donor_initialization():

    proper_donations_list = [Donation(100), Donation(200), Donation(300)]

    d1 = Donor("Bob", proper_donations_list)
    assert d1.donor_name == "Bob"
    assert d1.donations_list == proper_donations_list

    # Check Non proper list is proved
    d2 = Donor("Ted", [Donation(100), 2, "Red"])
    assert d2.donor_name == "Ted"
    assert d2.donations_list == []

    # Check No list is provided
    d3 = Donor("Sam")
    assert d3.donor_name == "Sam"
    assert d3.donations_list == []


def test_donor_add_donation():
    d1 = Donor("Bob", [Donation(100)])

    d1.add_donation(200)
    curr_time = datetime.datetime.now()

    # Check length of list, and attributes of the added donation object
    assert len(d1.donations_list) == 2
    assert d1.donations_list[1].amount == 200
    assert d1.donations_list[1].date == curr_time


def test_donor_send_mail_latest():
    d1 = Donor("Bob", [Donation(100), Donation(200)])
    assert d1.send_mail_latest() == 'dear donor Bob the last donation is 200'


def test_donor_total_donation():
    d1 = Donor("Bob", [Donation(100), Donation(200), Donation(300)])
    assert d1.total_donation() == 600


def test_donor_number_of_gifts():
    d1 = Donor("Bob", [Donation(100), Donation(200), Donation(300)])
    assert d1.number_of_gifts() == 3


def test_donor_average_donation_amount():
    d1 = Donor("Bob", [Donation(100), Donation(200), Donation(300)])
    assert d1.average_donation_amount() == 200


def test_donor_print_donations_list():
    d1 = Donor("Bob", [Donation(100), Donation(200), Donation(300)])
    curr_time = datetime.datetime.now()

    assert d1.print_donations_list() == "{} on {} | {} on {} | {} on {} | "\
        .format(100, curr_time, 200, curr_time, 300, curr_time)


# Test Charity Class
def setup_initial_charity():
    """Helper function for setting up charity for unit tests"""
    new_donor1 = Donor("Fred")
    new_donor1.add_donation(100)
    new_donor1.add_donation(1000)
    new_donor1.add_donation(10000)

    new_donor2 = Donor("Bob")
    new_donor2.add_donation(200)
    new_donor2.add_donation(2000)
    new_donor2.add_donation(20000)

    new_charity = Charity("Foundation")
    new_charity.add_donor(new_donor1.donor_name, new_donor1.donations_list)
    new_charity.add_donor(new_donor2.donor_name, new_donor2.donations_list)
    return new_charity


# This test includes init test
def test_charity_add_donor():
    new_donor1 = Donor("Fred")
    new_donor1.add_donation(100)
    new_donor1.add_donation(1000)
    new_donor1.add_donation(10000)

    new_donor2 = Donor("Bob")
    new_donor2.add_donation(200)
    new_donor2.add_donation(2000)
    new_donor2.add_donation(20000)

    # Checks init()
    new_charity = Charity("Foundation")
    assert new_charity.charity_name == "Foundation"
    assert new_charity.donors_dict == {}

    # Checks add_donor()
    new_charity.add_donor(new_donor1.donor_name, new_donor1.donations_list)
    new_charity.add_donor(new_donor2.donor_name, new_donor2.donations_list)

    assert new_charity.donors_dict["Fred"].donor_name == "Fred"
    assert new_charity.donors_dict["Fred"].donations_list == new_donor1.donations_list

    assert new_charity.donors_dict["Bob"].donor_name == "Bob"
    assert new_charity.donors_dict["Bob"].donations_list == new_donor2.donations_list

    # Checks print_total_donations()
    assert new_charity.print_total_donations() == "Donor {} : Total amount is {}\nDonor {} : Total amount is {}\n"\
                                                .format("Fred", 11100, "Bob", 22200)

def test_charity_get_donation_list():
    new_charity = setup_initial_charity()

    assert new_charity.get_donation_list() == "Donor: Fred                    Donations: 100, 1000, 10000\n" \
                                            "Donor: Bob                     Donations: 200, 2000, 20000\n"

def test_charity_generate_letter_text():
    new_charity = setup_initial_charity()
    assert new_charity.generate_letter_text(new_charity.donors_dict["Fred"]) == ('Dear {:},\n'
                                                         '\n'
                                                         '      Thank you for your very kind donation of ${:.2f}.\n'
                                                         '      It will be put to very good use.\n'
                                                         '\n'
                                                         '                      Sincerely,\n'
                                                         '                          -The Team').format("Fred", 11100)

def test_charity_send_letters_to_all_donors_files_exists():
    new_charity = setup_initial_charity()
    new_charity.send_letter_to_all_donors()

    curr_directory = os.getcwd()
    file_1 = os.path.join(curr_directory, "Fred_TY_letter.txt")
    file_2 = os.path.join(curr_directory, "Bob_TY_letter.txt")

    assert os.path.isfile(file_1)
    assert os.path.isfile(file_2)

    # Clean up
    os.remove(file_1)
    os.remove(file_2)


def test_charity_create_report():
    new_charity = setup_initial_charity()

    table_list = list()
    table_list.append("Donor Name                | Total Given | Num Gifts | Average Gift")
    table_list.append("------------------------------------------------------------------")
    table_list.append("Bob                        $    22200.00          3  $     7400.00")
    table_list.append("Fred                       $    11100.00          3  $     3700.00")

    print(new_charity.create_report())

    assert new_charity.create_report() == table_list



if __name__ == "__main__":
    pytest.main([__file__])