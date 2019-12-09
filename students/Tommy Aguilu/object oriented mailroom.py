### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A

import math
donor_raw = {"Mark Zuckerberg" : [32432, 38475, 7845], "Jeff_Bezos" : [23424, 234324, 444432, 222341], "Paul Allen" : [23424, 234324, 44432, 2341], "Melinda Gates" : [3432, 26524, 44432, 22741]}

class donor_cleaned():
    def __init__(self,**kwargs):
        self.donations = kwargs
    def cleanup(self):
        x = []
        for k,v in self.donations.items():
            y = []
            y.append(k)
            for i in v:
                y.append(i)
            x.append(y)
            print(y)
        return x

#key = donor, values = all donations
donor_processed = []
def list_reader(list1):
    print(list1)
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

def clean_data(donor_raw):
    #Creates list of list
    x = []
    for key, value in donor_raw.items():
        y = []
        y.append(key)
        y.append(sum(value)) #total donations
        y.append(len(value)) #number of donations
        y.append((sum(value)/len(value)).__round__()) #avg donations
        x.append(y)
    return x

if __name__ == "__main__":
    donor_processed = clean_data(donor_raw)
    sentinal = True
    while sentinal == True:
        choice = input("1. Print Donor Report \n2. Send Letter\n3. Close out\n4. Initiate unit tests\n""What would you like to do?")
        if choice == str(1):
            list_reader(donor_processed)
        elif choice == str(2):
            donor_list(donor_raw)
            donor_choice = input("Which donor would you like to write a thank you to? (type all if you would like to send it a letter to all) ")
            if donor_choice in donor_raw:
                donor_letter(donor_raw,donor_choice)
            if donor_choice == "all":
                send_many(donor_raw)
            elif donor_processed not in donor_raw:
                donation_list = []
                donation = input("Donor not found in list please specify how donation amount")
                donation_list.append(donation)
                donor_raw.update({donor_choice : donation_list})
                donor_letter(donor_raw,donor_choice)
        elif choice == str(3):
            print("closing out")
            sentinal = False
        elif choice == str(4):
            #testing.test()
            print("fix texting :(")


