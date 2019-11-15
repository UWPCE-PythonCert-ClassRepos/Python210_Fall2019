# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:09:10 2019

@author: joejo
"""


def colors(fore_color = 'red', back_color = 'orange', link_color = 'blue', visited_color = 'green'):
    info = f'The fore_color is {fore_color}, back_color is {back_color}, link_color is ' \
    + f'{link_color}, and the visited_color is {visited_color}'
    return info


def colors2(*args, **kwargs):
    print('The args are :', args)
    print('The kwargs are: ', kwargs)
    return args, kwargs