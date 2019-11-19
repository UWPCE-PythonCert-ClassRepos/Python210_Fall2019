# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:11:23 2019

@author: joejo
"""


from colors import colors, colors2


def test_pos():
    assert colors('red', 'blue', 'yellow', 'chartreuse') == \
    'The fore_color is red, back_color is blue, link_color is yellow, and the visited_color is chartreuse'


def test_key():
    assert colors(link_color='red', back_color='blue') == \
    'The fore_color is red, back_color is blue, link_color is red, and the visited_color is green'


def test_combo():
    assert colors('purple', link_color='red', back_color='blue') == \
    'The fore_color is purple, back_color is blue, link_color is red, and the visited_color is green'


def test_arbitrary():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert colors(*regular, **links) == \
    'The fore_color is red, back_color is blue, link_color is chartreuse, and the visited_color is green'


def test_pos2():
    colors = colors2('red', 'blue', 'yellow', 'chartreuse')
    assert colors[0] == ('red', 'blue', 'yellow', 'chartreuse')


def test_key2():
    colors = colors2(link_color='red', back_color='blue')
    assert colors[1]['link_color'] == 'red'
    assert colors[1]['back_color'] == 'blue'


def test_combo2():
    colors = colors2('purple', link_color='red', back_color='blue')
    assert colors[0][0] == 'purple'
    assert colors[1]['link_color'] == 'red'
    assert colors[1]['back_color'] == 'blue'


def test_arbitrary2():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    colors = colors2(*regular, **links)
    assert colors[0] == ('red', 'blue')
    assert colors[1].get('link_color') == 'chartreuse'