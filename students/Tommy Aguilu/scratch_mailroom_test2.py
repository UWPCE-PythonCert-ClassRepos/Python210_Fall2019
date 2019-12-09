import math
donor_raw = {"Jerry" : [32432, 38475, 7845], "Mark" : [432, 38575]}
class Donor():
    def __init__(self, name, donations):
        self.name = name
        self.donations = []
        if(isinstance(donations, (int,float))):
            self.donations = [donations]
        else:
            self.donations = donations
    def last_donation(self):
        return self.donations[-1]
    def average_donation(self):
        return (sum(self.donations)/len(self.donations)).__round__()
    def number_of_donations(self):
        return len(self.donations)
    def __str__(self):
        return ('Donor Name: {}, Donations: {}').format(self.name, self.donations)
    @staticmethod
    def list_reader(y):
        print("Donor Name                | Total Given | Num Gifts | Average Gift")
        print("------------------------------------------------------------------")
        for i in y:
            a = len(str(i[0]))
            b = len(str(i[1]))
            c = len(str(i[2]))
            d = len(str(i[3]))
            print(i[0] + ((28 - a) * " ") + str(i[1]) + ((13 - b) * " ") + str(i[2]) + ((13 - c) * " ") + str(i[3]) + (
                        (14 - d) * " "))
    @staticmethod
    def clean_list(donor_raw):
        x = []
        for k, v in donor_raw.items():
            donor = Donor(k, v)
            y = []
            y.append(k)
            y.append(donor.last_donation())
            y.append(donor.number_of_donations())
            y.append(donor.average_donation())
            x.append(y)

d1 = Donor(donor_raw)
print(d1)

