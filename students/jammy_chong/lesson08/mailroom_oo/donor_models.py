import os

class Donor:
    def __init__(self, DonorName, ListInitialDonations=None):
        self.DonorName = DonorName
        if type(ListInitialDonations) == list:
            self.Donations = ListInitialDonations
        elif type(ListInitialDonations) == (int or float):
            self.Donations = [ListInitialDonations]
        else:
            self.Donations = []

    def AddDonation(self, Amount):
        self.Donations.append(Amount)

    def AverageDonation(self):
        return sum(self.Donations)/len(self.Donations)

    def TotalDonation(self):
        return sum(self.Donations)

    def LatestDonation(self):
        return (f'Dear {self.DonorName}, your last donation was ' +
                f'{self.Donations[-1]}')

    def SendEmail(self):
        times = "times"
        if len(self.Donations) < 2:
            times = "time"
        return f"Dear {self.DonorName},\n\n\tYou have donated " + \
               f"{len(self.Donations)} {times} with an average of $" + \
               f"{self.AverageDonation():.2f} per donation.\n\n\tThe total " + \
               f"amount you donated is ${self.TotalDonation():.2f}, and " + \
               f"your last donation was ${self.Donations[-1]:.2f}.\n\n\tIt " + \
               f"will be put to very good use.\n\n\t\t\t" + \
               f"Sincerely,\n\t\t\t\t-The Team."

    def TextFile(self, path, date=""):
        with open(path + self.DonorName + '_' + date + '.txt', 'w') as f:
            f.write(self.SendEmail())
            f.close()

    def __lt__(self, other):
        if isinstance(other, Donor):
            return (self.TotalDonation() < other.TotalDonation())

class Charity:
    def __init__(self, Name):
        self.CharityName = Name
        self.DonorList = {}

    def AddDonor(self, DonorName, ListDonations):
        self.DonorList[DonorName] = Donor(DonorName, ListDonations)

    def GetDonorNames(self):
        DonorNames = []
        for donor in self.DonorList:
            DonorNames.append(donor)
        return DonorNames

    def GetDonorList(self):
        DonorNames = self.GetDonorNames()
        string_line = "-" * 30 + "\n"
        string_list = string_line
        string_list += "\n".join(DonorNames) + "\n"
        string_list += string_line
        return string_list

    def GetReport(self):
        sorted_list = sorted(self.DonorList.items(),
                             key=lambda e: e[1].TotalDonation(), reverse=True)
        dashedLine = "-"*59 + "\n"
        report = dashedLine + "{}\n".format(self.CharityName) + \
                 dashedLine + "Donor Name" + " "*9 + \
                 "| Total Given | Num Gifts | Average Gift\n" + dashedLine
        for donor in sorted_list:
            report += "{:18}  ${:>11.2f}{:>12d}  ${:>12.2f}".format(
                      donor[1].DonorName, donor[1].TotalDonation(),
                      len(donor[1].Donations), donor[1].AverageDonation()) +"\n"
        return report

    def CreateTextFiles(self, path, date=""):
        for donor in self.DonorList: donor.TextFile(path, date)
