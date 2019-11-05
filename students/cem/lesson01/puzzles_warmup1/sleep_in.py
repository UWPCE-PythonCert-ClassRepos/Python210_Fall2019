"""
sleep_in @ https://codingbat.com/prob/p173401
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


weekday_and_vacation = sleep_in(weekday=True, vacation=True)
weekday_and_not_vacation = sleep_in(weekday=True, vacation=False)
not_weekday_not_vacation = sleep_in(weekday=False, vacation=False)
not_weekday_and_vacation = sleep_in(weekday=False, vacation=True)

print("Today is weekday and you are on vacation the which results in the function being:", weekday_and_vacation,
". You deserve a sleep in.")

print("Today is a weekday and you are not on vacation which results in the function being:", weekday_and_not_vacation,
      ". It's not the right day for a sleep in! Wake up and go do something useful!")

print("Today is not a weekday and you are not on vacation which results in the function being:", not_weekday_not_vacation,
      ". You deserve a sleep in.")

print("Today is not a weekday and you are on vacation which results in the function being:", not_weekday_and_vacation,
      ". You deserve a sleep in.")
