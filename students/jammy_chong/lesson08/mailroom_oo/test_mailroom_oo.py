import pytest
import pathlib
from donor_models import Donor, Charity

def test_Donor_1():
    d = Donor("Jeff Bezos", [1000.00, 42500, 60000.00])
    assert d.DonorName == "Jeff Bezos"
    assert d.Donations == [1000.00, 42500, 60000.00]

def test_Donor_2():
    d = Donor("Jeff Bezos", 100)
    assert d.Donations == [100]
    d = Donor("Jeff Bezos")
    assert d.Donations == []
    d = Donor("Jeff Bezos", "amazon")
    assert d.Donations == []

def test_Donor_3():
    d = Donor("Jeff Bezos", [1000.00])
    d.AddDonation(5000)
    assert d.Donations == [1000.00, 5000]
    assert d.TotalDonation() == 6000.00

def test_Donor_4():
    d = Donor("Jeff Bezos", [4000.00, 2345])
    assert d.LatestDonation() == f"Dear Jeff Bezos, your last donation was 2345"
    email = "Dear Jeff Bezos,\n\n\tYou have donated 2 times with an average" + \
            " of $3172.50 per donation.\n\n\tThe total amount you donated " + \
            "is $6345.00, and your last donation was $2345.00.\n\n\tIt will " + \
            "be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t\t-The Team."
    assert d.SendEmail() == email
    d.TextFile("./", "today")
    file = pathlib.Path('./Jeff Bezos_today.txt')
    assert file.exists() is True

def test_Donor_5():
    dlist = [Donor("Bill Gates", [32000, 12000, 40000]),
            Donor("Paul Allen", [1000000]),
            Donor("Jeff Bezos", [400, 500]),
            Donor("Steve Jobs", [50000, 1000, 4000])]
    dlist.sort()
    dlist.reverse()
    list_string = ""
    for name in dlist:
        list_string += name.DonorName + ": " + str(name.TotalDonation()) + ".\n"
    assert list_string == "Paul Allen: 1000000.\nBill Gates: 84000.\n" + \
                          "Steve Jobs: 55000.\nJeff Bezos: 900.\n"


def test_Charity_1():
    c = Charity("Red Cross")
    c.AddDonor("Bill Gates", [10000, 5000.00, 42000.00])
    c.AddDonor("Jeff Bezos", [1500.00])
    c.AddDonor("Paul Allen", [50000])
    assert c.CharityName == "Red Cross"
    assert "Bill Gates" in c.DonorList
    c.DonorList["Paul Allen"].AddDonation(4500.00)
    assert c.DonorList["Paul Allen"].Donations == [50000, 4500.00]
    DonorInfo = list()
    for donor in c.DonorList.items():
        DonorInfo.append(f"{donor[1].DonorName}: {donor[1].TotalDonation():.2f}")
    assert ",".join(DonorInfo) == "Bill Gates: 57000.00," + \
                                  "Jeff Bezos: 1500.00," + \
                                  "Paul Allen: 54500.00"

def test_Charity_2():
    c = Charity("Red Cross")
    c.AddDonor("Bill Gates", [10000, 5000.00, 42000.00])
    c.AddDonor("Jeff Bezos", [1500.00])
    c.AddDonor("Paul Allen", [50000, 4500.00])
    DonorList = c.GetDonorList()
    assert DonorList == "------------------------------\n" + \
                        "Bill Gates\nJeff Bezos\nPaul Allen\n" + \
                        "------------------------------\n"

def test_Charity_3():
    c = Charity("Red Cross")
    c.AddDonor("Bill Gates", [10000, 5000.00, 42000.00])
    c.AddDonor("Jeff Bezos", [1500.00])
    c.AddDonor("Paul Allen", [50000, 4500.00])
    Report = "-----------------------------------------------------------\n" + \
             "Red Cross\n" + \
             "-----------------------------------------------------------\n" + \
             "Donor Name         | Total Given | Num Gifts | Average Gift\n" + \
             "-----------------------------------------------------------\n" + \
             "Bill Gates          $   57000.00           3  $    19000.00\n" + \
             "Paul Allen          $   54500.00           2  $    27250.00\n" + \
             "Jeff Bezos          $    1500.00           1  $     1500.00\n"
    assert c.GetReport() == Report
