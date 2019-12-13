import math
donor_raw = {"Jerry" : [32432, 38475, 7845], "Mark" : [432, 38575]}
class donor():
    def __init__(self, donation_name):
        self.donation_name = donation_name[0]
        self.last_donation = donation_name[1]
    def total_dontations(self,donation_list):
        return sum(donation_list)
    def average_donation(self, donation_list):
        return sum(donation_list)/len(donation_list).__round__()
    def count_gifts(self,donation_list):
        return len(donation_list)
    def __str__(self):
        return f"Dear {self.donation_name},\n thank you for your donation of {self.last_donation} dollars"

class DonorCollection():
    def __init__(self, donor_name, donation_totals, donation_numbers, average_donations):
        self.donor_name = donor_name
        self.donation_totals = donation_totals
        self.donation_numbers = donation_numbers
        self.average_donations = average_donations


donor_list = ["harry", [45,56,77]]
x = donor(donor_list)
print(x.average_donation(donor_list[1]))
print(x.count_gifts(donor_list[1]))
print(x.total_dontations(donor_list[1]))

b = DonorCollection(x.donation_name, x.total_dontations(donor_list[1]), x.count_gifts(donor_list[1]),
                x.average_donation(donor_list[1]))
print(b.donor_name)
print(b.donation_totals)
print(b.donation_numbers)
print(b.average_donations)
