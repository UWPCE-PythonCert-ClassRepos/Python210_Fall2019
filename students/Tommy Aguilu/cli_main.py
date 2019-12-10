from donor_models import donor
from donor_models import  donor_collection
from test_mailroom_oo import tests

def create_donor_data():
    d1 = donor("Mark Zuckerberg")
    d1.new_donation(3245)
    d1.new_donation(48372)
    d2 = donor("Bill Gates")
    d2.new_donation(43454)
    d2.new_donation(444)
    d2.new_donation(23444)
    a = donor_collection(d1.return_list())
    a.add_donor(d2.return_list())
    return a

a = create_donor_data()
sentinal = True
while sentinal == True:
    choice = input("1. Print Donor Report \n2. Write Letter\n3. Initiate unit tests\n4. Close out\n""What would you like to do?")
    if choice == "1":
        a.report_writer()
    elif choice == "2":
        print("")
    elif choice == "3":
        tests()
    elif choice == "4":
        break