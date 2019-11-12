import math
donor_raw = {"Mark Zuck" : [578, 86, 77], "Mark b" : [578, 86, 77, 67543]}
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
    for key in donor_list:
        print(key)
def donor_letter(donor_raw,donor_choice):
    donations = (donor_raw[donor_choice])
    donations_output = donations[-1]
    print("thank you {} for your most recent donation of {}".format(donor_choice, donations_output))

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
    if choice == str(1):
        list_reader(donor_processed)
    elif choice == str(2):
        donor_list(donor_raw)
        donor_choice = input("Which donor would you like to write a thank you to?")
        if donor_choice in donor_raw:
            donor_letter(donor_raw,donor_choice)
        else:
            donation_list = []
            donation = input("Donor not found in list please specify how donation amount")
            donation_list.append(donation)
            donor_raw.update({donor_choice : donation_list})
            donor_letter(donor_raw,donor_choice)
    elif choice == str(3):
        print("closing out")
        sentinal = False