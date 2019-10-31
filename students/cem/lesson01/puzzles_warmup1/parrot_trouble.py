"""
parrot_trouble @ https://codingbat.com/prob/p166884
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
"""


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


parrot_talking_before_7 = parrot_trouble(talking=True, hour=3)
parrot_talking_after_7 = parrot_trouble(talking=True, hour=9)
parrot_talking_after_20 = parrot_trouble(talking=True, hour=21)

print("Parrot talking at 3am. Are we in trouble?", parrot_talking_before_7)
print("Parrot talking at 9am. Are we in trouble?", parrot_talking_after_7)
print("Parrot talking at 9pm. Are we in trouble?", parrot_talking_after_20)
