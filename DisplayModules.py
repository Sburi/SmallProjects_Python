# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:48:38 2018

@author: steve
"""

print("This sub will list all available installed modules")
usr_SeeWarnings = input("Would you like to see warnings? Enter Y or N: ")
if usr_SeeWarnings == "N":
    import warnings
    warnings.filterwarnings("ignore")
help("modules")
input("Note, the above list is not searchable. Press enter to close.")