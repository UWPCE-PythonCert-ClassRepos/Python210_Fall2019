import Mailroom04 as m


m.donor_list = dict()
m.add_donor("Jammy Chong", [1200.00, 2400.00])
m.add_donor("David Pokrajac", [3600.00, 850.00, 350.00])
m.add_donor('John Smith', [1200.00, 1500.00])


def test_add_donor():
    assert ('David Pokrajac' in m.donor_list) is True
    assert m.donor_list['David Pokrajac'][-1] == 350.00


def test_create_letter():
    letter = "Dear John Smith,\n\n\tThank you for your very kind donation of " + \
    "$1500.00.\n\n\tYou have donated 2 times with an average of $1350.00 per " + \
    "donation.\n\n\tThe total amount you donated is $2700.00.\n\n\tIt will be " + \
    "put to very good use.\n\n\t\t\tSincerely,\n\t\t\t\t-The Team."
    assert m.create_letter('John Smith') == letter


def test_display_donor_list():
    display_text = "------------------------------\n" + \
                   "Jammy Chong\nDavid Pokrajac\nJohn Smith\n" + \
                   "------------------------------"
    assert m.display_donor_list() == display_text

def test_create_report():
    print(m.donor_list)
    text = "Donor Name                | Total Given | Num Gifts | Average Gift\n" + \
           "------------------------------------------------------------------\n" + \
           "David Pokrajac             $    4800.00           3  $     1600.00\n" + \
           "Jammy Chong                $    3600.00           2  $     1800.00\n" + \
           "John Smith                 $    2700.00           2  $     1350.00\n"
    assert m.display_report() == text

def test_create_text_files():
    m.create_text_files('./', "11252019")
    file1 = m.pathlib.Path('./David Pokrajac_11252019.txt')
    file2 = m.pathlib.Path('./Jammy Chong_11252019.txt')
    file3 = m.pathlib.Path('./John Smith_11252019.txt')
    assert file1.exists() is True
    assert file2.exists() is True
    assert file3.exists() is True
