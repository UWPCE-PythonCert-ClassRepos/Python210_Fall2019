# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:29:40 2019

@author: joejo

answers to Python Warm Ups 2
https://codingbat.com/python/Warmup-2
"""

def string_times(str, n):
  return str * n

def front_times(str, n):
  return str[:3] * n #slice is silent about missing characters (in the case that len(str)<3)

def string_bits(str):
  return str[::2]

def string_splosion(str):
  str2 = ''
  for i in range(len(str)):
    str2 = str2 + str[:i+1]
  return str2

def last2(str):
  last_two = str[-2:]
  n = 0
  for i in range(2,len(str)):
    if last_two in str[i-2:i]:
      n += 1
  return n

def array_count9(nums):
  n = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      n += 1
  return n

def array_front9(nums):
  ans = 9 in nums[:3]
  return ans

def array123(nums):
  temp = False
  for i in range(len(nums)-2):
    if nums[i:i+3] == [1,2,3]:
      temp = True
  return temp

def string_match(a, b):
  lim = min(len(a), len(b))
  count = 0
  for i in range(2,lim+1):
    if a[i-2:i] == b[i-2:i]:
      count += 1
  return count