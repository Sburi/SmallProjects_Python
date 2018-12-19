# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:12:17 2018

@author: 431165
"""

#Purpose:
print("\nThis program guesses gender based on height, weight, and shoe size.")

#Dependencies
from sklearn import tree

#Metric or Customary/Standard
Mod_Shoe = 0
UsingMetric = input("\nWill you be using metric? Enter Y or N: ") #Only built to support metric or standard or customary
if UsingMetric == "N":
    Mod_Shoe = 38
    uHeight = float(input("What is your total height in inches? "))
else:
    uHeight = float(input("What is your total height in centimeters? "))
    
#User Inputs
uWeight = float(input("What is your weight? "))
uShoeSize = float(input("What is your shoe size? ")) + Mod_Shoe

#Inputs
#[height, weight, shoesize]
X = [[181, 80, 44], [177,70,43], [160, 60, 38], [154, 54, 37],
    [16, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
    [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ["Male", "Female", "Female", "Female", "Male", "Male",
     "Male", "Female", "Male", "Female", "Male"]

#Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
prediction = clf.predict([[uHeight, uWeight,  uShoeSize]])

#Print Prediction
print("\nBased on your inputs, I believe you are a " + str(prediction[0]).lower() + ".")

#Wait before closing
input("\nPress enter to close")