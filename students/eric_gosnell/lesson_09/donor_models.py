"""
Eric Gosnell
Lesson 9 - Object Oriented Mailroom
12.10.2019

        ****    Classes only   ****
"""

from functools import total_ordering

if __name__ == "__main__":
    raise Exception("This file is not meant to be run by itself.")


@total_ordering
class Donor:
    def __init__(self, name, donations=None):
        self._name = name.upper()
        if donations is not None:
            self._donations = donations
        else:
            self._donations = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def __eq__(self, other):
        return self.sum_donations == other.sum_donations

    def __lt__(self, other):
        return self.sum_donations < other.sum_donations

    def add_donation(self, date, donation):
        new_donation = {date: donation}
        self._donations.append(new_donation)

    @property
    def sum_donations(self):
        donations_numeric_only = []
        for donation in self._donations:
            for k, v in donation.items():
                donations_numeric_only.append(v)
        return sum(donations_numeric_only)

    @property
    def qty_donations(self):
        return int(len(self._donations))

    @property
    def avg_donation(self):
        try:
            average_donation = self.sum_donations / self.qty_donations
            return average_donation
        except ZeroDivisionError:
            return 0

    @property
    def thank_you_email(self):
        first_name, last_name = self._name.split()
        message = (f"Thank you {first_name.capitalize()} {last_name.capitalize()}.\n"
                   f"We greatly appreciate your recent donation of ${self.recent_donation:,.2f}\n"
                   f"received on {self.recent_date}.\n"
                   "It will be put to good use.\n"
                   "\t\t\tSincerely,\n"
                   "\t\t\t\t-The Team")
        return message

    @property
    def recent_date(self):
        date = str(self.donations[-1])
        return date[2:12].translate({95: 47})  # date part of dictionary record

    @property
    def recent_donation(self):
        donation = str(self.donations[-1])
        return float(donation[15:-1])   # numeric part of dictionary record

    @property
    def donations(self):
        return self._donations

    @property
    def name(self):
        first, last = self._name.split()
        formatted_name = f'{first.capitalize()} {last.capitalize()}'
        return formatted_name


class Charity:
    def __init__(self, name):
        self._donors = []
        self._name = name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def add_donor(self, donor):
        self._donors.append(donor)

    @property
    def donor_list(self):
        return self._donors

    @property
    def name(self):
        return self._name
