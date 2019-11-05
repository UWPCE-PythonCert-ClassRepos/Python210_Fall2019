# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:33:47 2019

@author: joejo

answers to Python Warm Ups 1
https://codingbat.com/python/Warmup-1
"""

#SleepIn
def sleep_in(weekday, vacation):
  if vacation:
    return True
  elif weekday:
    return False
  else:
    return True

#monkeys
def monkey_trouble(a_smile, b_smile):
  temp = a_smile ^ b_smile
  return not temp

#sum or double sum
def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return (a + b) * 2

def diff21(n):
  if n>21:
    return (n-21)*2
  else:
    return 21-n

def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
    else:
      return False
  else:
    return False

def makes10(a, b):
  if a == 10 or b == 10 or a+b==10:
    return True
  else:
    return False

def near_hundred(n):
  a = abs(100 - n)
  b = abs(200 - n)
  if a <= 10 or b <= 10:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if negative:
    if a<0 and b<0:
      return True
    else:
      return False
  else:
    if (a < 0) ^ (b < 0):
      return True
    else:
      return False

def not_string(str):
  if 'not' in str[0:3]:
    return str
  else:
    return ('not ' + str)

def missing_char(str, n):
  return (str[0:n] + str[n+1:])

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return (str[-1] + str[1:-1] + str[0])

def front3(str):
  if len(str) < 3:
    return str + str + str
  else:
    return str[0:3]*3
