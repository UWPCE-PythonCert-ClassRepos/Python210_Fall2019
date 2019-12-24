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
    assert joe_two.send_last_donation_email() == ('name_abcde',
                                                    'Heyyyy... name_abcde,\n\nThanks for the $4.00 sucka!\nKeep sending that money, though\n                  OK, BAIIII!')   

#Test charity class

def test_charity_init():
    NewTestCharity=mr_class.charity("This_is_charity_name")
    assert NewTestCharity.CharityName == "This_is_charity_name"

def test_charity_Donors_property_none():
    NewTestCharity=mr_class.charity("This_is_charity_name")
    assert NewTestCharity.Donors == {}

def test_charity_list_donors_property_none():
    NewTestCharity=mr_class.charity("This_is_charity_name")
    assert NewTestCharity.list_donors() == []

## mock for next few test
NewTestCharity=mr_class.charity("This_is_charity_name")
NewTestCharity.add_donor("DonaldDuck",[10,20,30])

def test_charity_list_donors_property():
    assert NewTestCharity.list_donors() == ['DonaldDuck']

def test_add_donor_to_existing():
    NewTestCharity.add_donor("Mickey",[40])
    assert str(NewTestCharity.Donors) == "{'DonaldDuck': DonaldDuck, [10, 20, 30], 'Mickey': Mickey, [40]}"

def test_add_create_report():
    NewTestCharity.add_donor("MARKYMARK",[40, 20, 10])
    assert NewTestCharity.create_report() == ('Donor Name               | Total Given      | Num Gifts      | Average Gift',
                                                '---------------------------------------------------------------------------',
                                                ['MARKYMARK                        70.00               3                23.33',
                                                'DonaldDuck                       60.00               3                20.00',
                                                'Mickey                           40.00               1                '
                                                '40.00'])

def test_send_letter_all():
    assert NewTestCharity.send_letter_all() == [('MARKYMARK',
                                                'Heyyyy... MARKYMARK,\n\nThanks for the $10.00 sucka!\nKeep sending that money, though\n                  OK, BAIIII!'),
                                                ('DonaldDuck',
                                                'Heyyyy... DonaldDuck,\n\nThanks for the $30.00 sucka!\nKeep sending that money, though\n                  OK, BAIIII!'),
                                                ('Mickey',
                                                'Heyyyy... Mickey,\n\nThanks for the $40.00 sucka!\nKeep sending that money, though\n                  OK, BAIIII!')]