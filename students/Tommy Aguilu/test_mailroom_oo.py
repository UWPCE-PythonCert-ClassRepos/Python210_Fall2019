from donor_models import donor
from donor_models import  donor_collection


def tests():
    a = donor("mark")
    a.new_donation(14)
    #donor class test section
    #tests for individual unit inputs
    assert a.donor_name == "mark"
    assert a.donor_values == [14]
    assert type(a.donor_values) == list
    a.new_donation(48)
    #assert a.last_donation == [48]
    #donor_collection section
    #tests for donor_collection methods
    print("\ntests pass!")
