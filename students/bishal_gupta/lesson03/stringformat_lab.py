#!/usr/bin/env python3
"""
Created on Tue Oct 29 17:24:46 2019

@author: Bishal.Gupta
"""


#Task one
#Input string: ( 2, 123.4567, 10000, 12345.67)
#Expected Output string: file_002 :   123.46, 1.00e+04, 1.23e+04
def string_format_using_format(n):
    #print ('file_{:03}) : {:.2f}, {:.2E}, {:.2E}' .format(2, 123.4567, 10000, 12345.67))
    return'file_{:03}) : {:.2f}, {:.2E}, {:.2E}' .format(2, 123.4567, 10000, 12345.67)

#Task two
#Sames input ande expected out as task one but using fstring function
def string_format_using_fstring(n):
    #print('file_{2:03} :   {123.4567:.2f}, {10000:.2E}, {12345.67:.2E}')
    return f'file_{2:03} :   {123.4567:.2f}, {10000:.2E}, {12345.67:.2E}'
#Task Three
#Inout:  (1,2,3)
#Expected output: the 3 numbers are: 1, 2, 3
def formatter(n):
    #print ("the " + str(len(n)) + " numbers are: " + len(n)*"{:d} ".format(*n))
    return "the " + str(len(n)) + " numbers are: " + len(n)*"{:d} ".format(*n)


#Task Four
#input: ( 4, 30, 2017, 2, 27)
#expected output: 02 27 2017 04 30   
def multi_element_formatter(n):
    #print("{:02} {:d} {:d} {:02} {:d}".format(n[3],n[4],n[2],n[0],n[1]))
    return "{:02} {:d} {:d} {:02} {:d}".format(n[3],n[4],n[2],n[0],n[1])
    
#Task Five
#Input: ['oranges', 1.3, 'lemons', 1.1]
#Exprected Output: The weight of an orange is 1.3 and the weight of a lemon is 1.1 
def f_string_in_play(t):
    #print ("The weight of an {t[0][:-1]:s} is {t[1]:.1f} and the weight of a {t[2][:-1]:s} is {t[3]:.1f}" )
    return "The weight of an {t[0][:-1]:s} is {t[1]:.1f} and the weight of a {t[2][:-1]:s} is {t[3]:.1f}"   

#Task six
#input: ‘First $99.01 Second $88.09 ‘
#output: 'First               $99.01    Second              $88.09  '   
#Will try dymanic lis later, will move on to Mailroom excercise to I don't fall behind espeically due to downtime due to my dental surgery   
# Will come back after getting some progress on Mailroom excercise
def f_row_and_columns(n):
    return '{:10}{:5}{:15}'.format(my_tuple[0],my_tuple[1])


if __name__ ==  "__main__":
    assert formatter(1,2,3) == 'the 3 numbers are: 1, 2, 3'
    assert multi_element_formatter(4, 30, 2017, 2, 27) == '02 27 2017 04 30'
