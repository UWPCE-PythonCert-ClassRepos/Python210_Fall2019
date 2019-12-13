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
    x = ("thank you {} for your most recent donation of {}".format(donor_choice, donations_output))
    return x

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

def test():
    test_set_raw = {"Mark Zuckerberg": [32432, 38475, 7845]}
    test_set_raw_multi = {"Mark Zuckerberg": [78752, 3, 26251],
                          "Jeff_Bezos": [23424, 234324, 444432, 222341]}
    assert clean_data(test_set_raw) == [["Mark Zuckerberg", 78752, 3, 26251]]
    assert type(clean_data(test_set_raw)) == list
    assert clean_data(test_set_raw_multi) == [['Mark Zuckerberg', 105006, 3, 35002], ['Jeff_Bezos', 924521, 4, 231130]]
    assert donor_letter(test_set_raw, "Mark Zuckerberg") == "thank you Mark Zuckerberg for your most recent donation of 7845"
    print("tests pass :)")