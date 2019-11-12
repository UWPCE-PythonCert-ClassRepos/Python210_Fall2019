def donor_list_print(donor):
    for key, value in donor.items():
        x = []
        x.append(key)
        counter = 0
        for i in value:
            x.append(value[counter])
            counter += 1
        print(x)


#donor_raw = {"Mark Zuck" : [578, 86, 77], "Mark b" : [578, 86, 77, 67543]}
#x = input("Who do you wanna pick")
#donations = (donor_raw[x])
#donations_output = donations[-1]
#donations_output = str(donations_output)
#print(donations_output)
x = "tom"
donations_output = "76"

print("thank you {} for your most recent donation of {}".format(x, donations_output))