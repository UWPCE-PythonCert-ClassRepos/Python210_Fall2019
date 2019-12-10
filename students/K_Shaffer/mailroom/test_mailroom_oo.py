import os.path
from donor_models import Charity
from donor_models import Donor

def main():
    # test Charity creation
    test_charity = Charity('local charity')
    assert(test_charity.CharityName == 'local charity')
    assert (test_charity.Donors == {})

    # test AddDonor from Charity
    test_name = 'Kyle Clark'
    test_charity.AddDonor(test_name)
    assert(test_charity.Donors[test_name].Donations == [])

    # test functions of Donor
    amount = 1000.56
    test_send_thank_you(test_charity, test_name, amount)

    # test send all thank yous of Charity
    test_send_all_thank_yous(test_charity)

def test_send_thank_you(local_charity, test_name, amount):
    local_charity.Donors[test_name].send_thank_you(amount)
    assert(local_charity.Donors[test_name].TotalDonations() == 1000.56)
    assert(local_charity.Donors[test_name].DonationCount() == 1)
    local_charity.Donors[test_name].AddDonation(amount)
    assert (local_charity.Donors[test_name].TotalDonations() == 2001.12)
    assert (local_charity.Donors[test_name].DonationCount() == 2)
    assert (local_charity.Donors[test_name].AverageDonation() == 1000.56)
    print('\n test_send_thank_you passed\n')

def test_send_all_thank_yous(local_charity):
    local_charity.send_all_thank_yous()
    for donor in local_charity.Donors:
        assert (os.path.exists('./' + donor + '_letter.txt'))
    print('\n test_send_all_thank_yous passed\n')

if __name__ == '__main__':
    main()