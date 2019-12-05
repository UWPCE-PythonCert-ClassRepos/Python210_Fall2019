import datetime
import os


class Donation:
    """
    Donation object contains amount and the date of when donation is created

    Attributes:
        amount (int): amount of money for the donation
        date   (int): timestamp of when donation is made/instantiated
    """
    def __init__(self, amount):
        self.amount = int(amount)
        self.date = datetime.datetime.now()

    def formatted_date(self):
        """Returns current date with just Month-Day-Year"""
        return self.date.strftime("%m-%d-%y")


class Donor:
    """
    This is a class for withholding each Donor's information

    Attributes:
        donor_name (str): donor's name
        donations {list): list of Donation objects
    """
    def __init__(self, donor_name, list_initial_donations=None):
        self.donor_name = donor_name

        # if not list, make new list otherwise create Donor with passed in Donor's Donation list
        if isinstance(list_initial_donations, list)\
                and all(isinstance(item, Donation) for item in list_initial_donations):
            self.donations_list = list_initial_donations
        else:
            self.donations_list = []

    def add_donation(self, amount):
        """Appends a new Donation to the Donor's Donations List
        """
        new_donation = Donation(amount)
        self.donations_list.append(new_donation)

    # Currently not in use
    def send_mail_latest(self):
        """Returns a formatted string of the Thank You letter to be sent to donor, includes latest donation
        """
        latest_donation = self.donations_list[-1]
        print('dear donor ' + str(self.donor_name) + ' the last donation is ' + str(latest_donation.amount))
        return ('dear donor ' + str(self.donor_name) + ' the last donation is '+ str(latest_donation.amount))


    def total_donation(self):
        """Provides the total amount the donor has donated
        """
        donation_amounts_list = [donation.amount for donation in self.donations_list]
        return sum(donation_amounts_list)


    def number_of_gifts(self):
        """Provides the number of donations gifts given"""
        return len(self.donations_list)

    def average_donation_amount(self):
        """Provides the average amount from the donations given"""
        return self.total_donation()/self.number_of_gifts()

    def print_donations_list(self):
        """Prints out donations, amount | timestamp"""
        donations_str = ''
        for donation in self.donations_list:
            print("{} on {} | ".format(donation.amount, donation.date))
            donations_str += "{} on {} | ".format(donation.amount, donation.date)
        return donations_str


class Charity:
    """
    Dictionary of Donor Objects {Donor Name : Donor Object}
    """
    def __init__(self, name):
        self.charity_name = name
        self.donors_dict = {}

    def add_donor(self, donor_name, donations_list=None):
        """Adds a donor object to the donors dictionary of the Charity object
        """
        self.donors_dict[donor_name] = Donor(donor_name, donations_list)

    # Currently not in use
    def print_total_donations(self):
        """Prints the total for each Donor in the Charity object"""
        total_str = ''
        for key, value in self.donors_dict.items():
            total_str += "Donor {} : Total amount is {}\n".format(key, str(value.total_donation()))
        print(total_str)
        return total_str

    def get_donation_list(self):
        """Returns a more legible formatted string of donors and their donation amounts
        """
        donation_list_print_string = ''

        for key, value in self.donors_dict.items():
            donation_list_print_string += "Donor: {:<20}    Donations: ".format(value.donor_name)
            for donation in value.donations_list:
                donation_list_print_string += "{}, ".format(donation.amount)

            #Removes extra comma and addes new line
            donation_list_print_string = donation_list_print_string[0:-2]
            donation_list_print_string += "\n"

        return donation_list_print_string

    def generate_letter_text(self, donor):
        """Generates texts for thank you letter text for donor"""
        letter_format = ('Dear {:},\n'
                         '\n'
                         '      Thank you for your very kind donation of ${:.2f}.\n'
                         '      It will be put to very good use.\n'
                         '\n'
                         '                      Sincerely,\n'
                         '                          -The Team')

        return letter_format.format(donor.donor_name, donor.total_donation())

    def send_letter_to_all_donors(self):
        """
        Creates a file for each donor within the current working directory.
        Then writes a thank you note within each file with the donor's name and
        donor's total donation amount
        """
        curr_directory = os.getcwd()

        for key, value in self.donors_dict.items():
            filename = value.donor_name + "_TY_letter.txt"
            curr_file = os.path.join(curr_directory, filename)

            with open(curr_file, "w") as f:
                f.write(self.generate_letter_text(value))

    def sort_donor_list_descending_amount(self):
        """Returns a list of the donors sorted by their descending total donation amount """

        total_donations_tup_list = [(value.donor_name, value.total_donation()) for key, value in self.donors_dict.items()]

        for i in range(0, len(total_donations_tup_list)):
            for j in range(0, len(total_donations_tup_list) - 1):
                if total_donations_tup_list[j][1] < total_donations_tup_list[j + 1][1]:
                    temp = total_donations_tup_list[j]
                    total_donations_tup_list[j] = total_donations_tup_list[j + 1]
                    total_donations_tup_list[j + 1] = temp

        return [donor for donor, donations in total_donations_tup_list]


    # @staticmethod
    # def sort_key(self):
    #     return self.donors_dict.items.value.total_donation()



    def create_report(self):
        """Creates a report of the Donors, Total Given, Number of donations given, and Average Donation
            Returns formatted String of the printed Report
        """
        table_title_format = "{:<26}{:14}{:12}{:>14}"
        table_entry_format = "{:<26} ${:>12.2f}{:11}  ${:>12.2f}"
        table_print_list = list()

        table_print_list.append(
            table_title_format.format("Donor Name", "| Total Given ", "| Num Gifts ", "| Average Gift"))

        table_print_list.append(table_title_format.format("-" * 26, "-" * 14, "-" * 12, "-" * 14))

        # Used old method that was created
        sorted_donor_list = self.sort_donor_list_descending_amount()

        # Attempt to use sort key static method
        #sorted_donor_list = sorted(self.donors_dict.keys(), key=self.sort_key)


        #print(self.donors_dict)
        #print(sorted_donor_list)

        for donor in sorted_donor_list:
            table_print_list.append(table_entry_format.format(donor,
                                                              self.donors_dict[donor].total_donation(),
                                                              self.donors_dict[donor].number_of_gifts(),
                                                              self.donors_dict[donor].average_donation_amount()))

        for row in table_print_list:
            print(row)

        return table_print_list

if __name__ == '__main__':

    new_donor1 = Donor("Fred")
    new_donor1.add_donation(100)
    new_donor1.add_donation(1000)
    new_donor1.add_donation(10000)

    new_donor2 = Donor("Bob")
    new_donor2.add_donation(200)
    new_donor2.add_donation(2000)
    new_donor2.add_donation(20000)

    new_donor3 = Donor("Todd")
    new_donor3.add_donation(300)
    new_donor3.add_donation(3000)
    new_donor3.add_donation(30000)

    new_donor4 = Donor("Sally")
    new_donor4.add_donation(400)
    new_donor4.add_donation(4000)
    new_donor4.add_donation(40000)

    new_donor5 = Donor("Becky")
    new_donor5.add_donation(500)
    new_donor5.add_donation(5000)
    new_donor5.add_donation(50000)


    new_charity = Charity("Foundation")
    new_charity.add_donor(new_donor1.donor_name, new_donor1.donations_list)
    new_charity.add_donor(new_donor2.donor_name, new_donor2.donations_list)
    new_charity.add_donor(new_donor3.donor_name, new_donor3.donations_list)
    new_charity.add_donor(new_donor4.donor_name, new_donor4.donations_list)
    new_charity.add_donor(new_donor5.donor_name, new_donor5.donations_list)
   # new_charity.print_total_donations()

    #new_charity.send_letter_to_all_donors()
    new_charity.create_report()
    #print(new_charity.get_donation_list())

    #print(new_charity.get_donation_list())

    # NewCharity = Charity("GatesFoundation")
    # NewCharity.AddDonor("DonaldDuck", [10,20,30])
    # NewCharity.AddDonor("Micky", [40])
    #
    # NewCharity.PrintTotalDonations()