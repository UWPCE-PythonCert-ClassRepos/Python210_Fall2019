### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A

import math
donor_raw = {"Mark Zuckerberg" : [32432, 38475, 7845], "Jeff_Bezos" : [23424, 234324, 444432, 222341], "Paul Allen" : [23424, 234324, 44432, 2341], "Melinda Gates" : [3432, 26524, 44432, 22741]}
#key = donor, values = all donations
donor_processed = []
def list_reader(list1):
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("------------------------------------------------------------------")
    for i in list1:
        a = len(i[0])
        b = len(str(i[1]))
        c = len(str(i[2]))
        d = len(str(i[3]))
        print(i[0] + ((28-a)*" ") + str(i[1]) + ((13-b)*" ") + str(i[2]) + ((13-c)*" ") + str(i[3]) + ((14-d)*" "))

def donor_list(donor_list):
    [print(i) for i in donor_list]

def donor_letter(donor_raw,donor_choice):
    donations = (donor_raw[donor_choice])
    donations_output = donations[-1]
    print("thank you {} for your most recent donation of {}".format(donor_choice, donations_output))

def send_many(donor_raw):
    try:
        for k in donor_raw:
            for k, v in donor_raw.items():
                with open(k, "w") as f:
                    length = (len(v)-1)
                    f.write(("thank you {} for your most recent donation of {}".format(k, v[length])))
                    f.close()
        print("letters sent!")
    except:
        print("File issue, please check input")


for key, value in donor_raw.items():
    x = []
    x.append(key)
    x.append(sum(value)) #total donations
    x.append(len(value)) #number of donations
    x.append((sum(value)/len(value)).__round__()) #avg donations
    donor_processed.append(x)

sentinal = True
while sentinal == True:
    choice = input("What would you like to do?\n1. Print Donor Report \n2. Send Letter\n3. Close out\n")
    try:
        if choice == str(1):
            list_reader(donor_processed)
        elif choice == str(2):
            donor_list(donor_raw)
            donor_choice = input("Which donor would you like to write a thank you to? (type all if you would like to send it a letter to all) ")
            if donor_choice in donor_raw:
                donor_letter(donor_raw,donor_choice)
            if donor_choice == "all":
                send_many(donor_raw)
            else:
                donation_list = []
                donation = input("Donor not found in list please specify how donation amount")
                donation_list.append(donation)
                donor_raw.update({donor_choice : donation_list})
                donor_letter(donor_raw,donor_choice)
        elif choice == str(3):
            print("closing out")
            sentinal = False
    except:
        print("Incorrect input please try again")