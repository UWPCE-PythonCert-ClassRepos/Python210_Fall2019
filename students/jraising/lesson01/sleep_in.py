def sleep_in(weekday, vacation):
  if not weekday and not vacation:
    return True
  elif weekday and not vacation:
    return False
  elif not weekday and vacation:
    return True
  elif weekday and vacation:
    return True
#blah