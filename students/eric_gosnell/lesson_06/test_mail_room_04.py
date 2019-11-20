"""
Eric Gosnell
Lesson 06 - pytest module for mail room 04 main module logic
11.19.2019
"""


import mail_room_04 as m4

# -------------    Database Tests    ------------- #

donor_db = m4.donor_db


def test_read_donor_true():
    assert donor_db['Brent Golden'] == [750.0, 250.0, 250.0]


def test_read_donor_false():
    assert donor_db['Shiloh Gardner'] != [5000]


def donor_in_db(name):
    if name in donor_db:
        return True
    else:
        return False


def test_donor_in_db():
    assert donor_in_db('Alanna Newton') is True


def test_donor_not_in_db():
    assert donor_in_db('Invalid Name') is False


def add_donation(name, donation):
    if name in donor_db:
        donor_db[name].append(donation)
        return True
    else:
        return False


def test_add_donation_user():
    assert add_donation(name='Marcel Torres', donation=24000) is True


def test_add_donation_no_user():
    assert add_donation(name='Invalid Name', donation=44400) is False


def most_recent_donation(name, donation):
    if donor_db[name][-1] == donation:
        return True
    else:
        return False


def test_most_recent():
    assert most_recent_donation('Alanna Newton', 75) is True


def test_not_most_recent():
    assert most_recent_donation('Shiloh Gardner', 5000) is False


# -------------    Valid Input Tests    ------------- #


def valid_name_logic(name):
    try:
        float(name)
        return False
    except ValueError:
        return True


def test_valid_name():
    assert valid_name_logic('a string') is True


def test_not_valid_name():
    assert valid_name_logic(2200) is False


def valid_donation_logic(donation):
    try:
        donation = float(donation)
        if donation <= 0:
            return False
    except ValueError:
        return False
    else:
        return True


def test_valid_donation():
    assert valid_donation_logic(3000.24) is True


def test_invalid_donation():
    assert valid_donation_logic('a string') is False


def test_negative_donation():
    assert valid_donation_logic(-499) is False


# -------------    File Operation Tests   ------------- #

THANK_YOU_EMAIL = ("Thank you {}.\n"
                   "We greatly appreciate your recent donation of ${:,.2f}.\n"
                   "It will be put to good use.\n"
                   "\t\t\tSincerely,\n"
                   "\t\t\t\t-The Team")


def file_write(name, mode, donation):
    file_name = name + '.txt'
    try:
        with open(file_name, mode) as file:
            file.write(THANK_YOU_EMAIL.format(name, donation))
            return True
    except IOError:
        return False


def test_file_written():
    assert file_write('Michael Scott', 'w', 4000) is True


def test_file_not_written():
    assert file_write('Michael Scott', 'r', 4000) is False


def message_in_file(file_name):
    with open(file_name) as file:
        return file.read()


def test_correct_message_in_file():
    message = message_in_file('Michael Scott.txt')
    assert message == THANK_YOU_EMAIL.format('Michael Scott', 4000)


# -------------    Report Tests   ------------- #

def test_sum_donation():
    name = 'Alanna Newton'
    assert sum(donor_db[name]) == 425.0


def test_not_sum_donation():
    name = 'Alanna Newton'
    assert sum(donor_db[name]) != 799.01


def test_qty_donation():
    name = 'Alanna Newton'
    assert len(donor_db[name]) == 4


def test_not_qty_donation():
    name = 'Alanna Newton'
    assert len(donor_db[name]) != 1


def avg_donation(total, qty):
    try:
        avg = total / qty
        return avg
    except ZeroDivisionError:
        return 0


def test_avg_donation():
    assert avg_donation(425, 4) == 106.25


def test_zero_donation():
    assert avg_donation(425, 0) == 0
