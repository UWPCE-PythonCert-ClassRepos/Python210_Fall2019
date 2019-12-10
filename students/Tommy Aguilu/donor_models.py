class donor:
    def __init__(self, donor_name):
        self.donor_name = donor_name
        self.donor_values = []

    def new_donation(self, amount):
        self.donor_values.append(amount)

    def last_donation(self):
        return self.donor_values[-1]

    def average_donation(self):
        return (sum(self.donor_values) / len(self.donor_values)).__round__()

    def number_of_donations(self):
        return len(self.donor_values)

    def total_donation(self):
        return sum(self.donor_values)
    def return_list(self):
        return [self.donor_name, self.total_donation(), self.number_of_donations(), self.average_donation()]
    def letter_output_test(self):
        return print(f' Dear {self.donor_name}\n Thank you for your most recent donation of {self.last_donation()} dollars. To date you'
                f' have donated {self.number_of_donations()} times for a total of {self.total_donation()} \n \n Regards, \n Tommy')
    def write_letter(self):
        f = open(self.donor_name + ".txt", "w")
        f.write(f' Dear {self.donor_name}\n Thank you for your most recent donation of {self.last_donation()} dollars. To date you'
            f' have donated {self.number_of_donations()} times for a total of {self.total_donation()} \n \n Regards, \n Tommy')

class donor_collection:
    def __init__(self, donor_list):
        self.donor_list = [donor_list]

    def add_donor(self, new_donor):
        self.donor_list.append(new_donor)

    def report_writer(self):
        print("Donor Name                | Total Given | Num Gifts | Average Gift")
        print("------------------------------------------------------------------")
        for i in self.donor_list:
            a = len(i[0])
            b = len(str(i[1]))
            c = len(str(i[2]))
            d = len(str(i[3]))
            print(i[0] + ((28 - a) * " ") + str(i[1]) + ((13 - b) * " ") + str(i[2]) + ((13 - c) * " ") + str(i[3]) + (
                    (14 - d) * " "))
