'''
Script: mailroomclasses
Date: 11/24/2019
Dev: Kory Shaffer
'''

class Charity:

    def __init__(self, name):
        self.CharityName = name
        self.Donors = {}

    def AddDonor(self, donor_name, donations):
        self.Donors[donor_name] = Donor(donor_name, donations)

    def send_thank_you(self, donor_name, amount):
        if donor_name in self.Donors:
            self.Donors[donor_name].AddDonation(amount)
        else:
            self.AddDonor(donor_name, [amount, ])

        f = open(donor_name + '_letter.txt', 'w+')
        f.write('\n Dear {:s},\n \n Thank you for your generous donation of ${:.2f}. \n \n Kind Regards, \n'
                ' Local Non-Profit \n'.format(donor_name, amount))

    def create_report(self):
        print('{:<20}|{:^13}|{:^11}|{:^14}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
        print('-'*60)
        for donor in self.Donors:
            print('{:<20} ${:>12.2f}{:>11}  ${:>12.2f}'.format(self.Donors[donor].DonorName,
                                                               self.Donors[donor].TotalDonations(),
                                                               self.Donors[donor].DonationCount(),
                                                               self.Donors[donor].AverageDonation()))

    def send_all_thank_yous(self):
        for donor in self.Donors:
            f = open(self.Donors[donor].DonorName + '_letter.txt', 'w+')
            f.write('\n Dear {:s},\n \n Thank you for your generous donations totaling ${:.2f}. \n \n Kind Regards, \n'
                    ' Local Non-Profit \n'.format(self.Donors[donor].DonorName, self.Donors[donor].TotalDonations()))

class Donor():
    def __init__(self, donor_name, initial_donations=None):
        self.DonorName = donor_name
        self.Donations = initial_donations

    def AddDonation(self, amount):
        self.Donations.append(amount)

    def TotalDonations(self):
        return sum(self.Donations)

    def DonationCount(self):
        return len(self.Donations)

    def AverageDonation(self):
        return sum(self.Donations)/len(self.Donations)


