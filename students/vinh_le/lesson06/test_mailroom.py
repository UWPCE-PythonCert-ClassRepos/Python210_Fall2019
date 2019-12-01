#from . import mailroom
import mailroom
import os
import pytest


def test_create_report():
    table_list = list()
    table_list.append("Donor Name                | Total Given | Num Gifts | Average Gift")
    table_list.append("------------------------------------------------------------------")
    table_list.append("Becky                      $    55500.00          3  $    18500.00")
    table_list.append("Sally                      $    44400.00          3  $    14800.00")
    table_list.append("Todd                       $    33300.00          3  $    11100.00")
    table_list.append("Bob                        $    22200.00          3  $     7400.00")
    table_list.append("Fred                       $    11100.00          3  $     3700.00")

    assert mailroom.create_report() == table_list


def test_send_letter_text():
    expected_letter_text = ('Dear Becky,\n'
                     '\n'
                     '      Thank you for your very kind donation of $55500.00.\n'
                     '      It will be put to very good use.\n'
                     '\n'
                     '                      Sincerely,\n'
                     '                          -The Team')

    assert mailroom.generate_letter_text("Becky") == expected_letter_text


def test_send_letter_file_creation():
    mailroom.send_letter_to_all_donors()

    for donor in mailroom.donor_dict:
        filename = donor + "_TY_letter.txt"
        assert os.path.isfile(filename)


def test_send_thank_you_text():
    ty_text = mailroom.generate_thank_you_text("Bob", 10000)
    assert(ty_text == "Thank You Bob for your donation of 10000.")


def test_get_donor_dictionary():
    assert mailroom.get_donor_dictionary() == mailroom.donor_dict


def test_get_donor_donation_list():
    assert mailroom.get_donor_donation_list("Bob") == mailroom.donor_dict["Bob"]


def test_add_donation():
    curr_len = len(mailroom.get_donor_donation_list("Bob"))
    mailroom.add_donation("Bob", 12345)
    assert len(mailroom.get_donor_donation_list("Bob")) == curr_len + 1
    assert mailroom.get_donor_donation_list("Bob")[-1] == 12345


# Adds a donor to the list, so it affects some other tests
def test_add_donor():
    mailroom.add_donor("Sam")
    assert "Sam" in mailroom.donor_dict
    assert mailroom.get_donor_donation_list("Sam") == []


def test_quit_program():
    assert mailroom.quit_program() == "quit"

# These functions are covered with other test cases
# def test_total_given():
# def test_get_num_gifts():
# def test_average_gift_amount():
# def sort_list_descending_amount():


if __name__ == "__main__":
    pytest.main([__file__])