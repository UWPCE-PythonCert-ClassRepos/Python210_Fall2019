# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:54:41 2019

@author: joejo
"""

def safe_input(prompt: str):
    try:
        user_input = input(prompt)
    except KeyboardInterrupt:
        return None
    else:
        return user_input


if __name__ == "__main__":
    safe_input("gimme some input: ")