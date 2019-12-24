import mailroom_oo_donor_models as mr_class

#Test donor class

def test_donor_init_name_only():
    joe = mr_class.donor("name_abcd")
    assert str(joe) == "name_abcd, None"

def test_donor_init_name_donations():
    joe_two = mr_class.donor("name_abcde",[1,2,3,4])
    assert str(joe_two) == "name_abcde, [1, 2, 3, 4]"

def test_add_donation_no_donations():
    joe = mr_class.donor("name_abcd")
    joe.add_donation(5)
    assert str(joe) == "name_abcd, [5]"
    
def test_add_donation_init_donations():
    joe_two = mr_class.donor("name_abcde",[1,2,3,4])
    joe_two.add_donation(5)
    assert str(joe_two) == "name_abcde, [1, 2, 3, 4, 5]"    

def test_average_donation():
    joe_two = mr_class.donor("name_abcde",[1,2,3,4])
    assert joe_two.average_donation() == 2.5

def test_total_donation():
    joe_two = mr_class.donor("name_abcde",[1,2,3,4])
    assert joe_two.total_donations() == 10    

def test_last_donation_email():
    joe_two = mr_class.donor("name_abcde",[1,2,3,4])
    assert joe_two.send_last_donation_email()   == ('name_abcde',
                                                    'Heyyyy... name_abcde,\n\nThanks for the $4.00 sucka!\nKeep sending that money, though\n                  OK, BAIIII!')   