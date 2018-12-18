# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:56:28 2018

@author: steve
"""

#Purpose
print("This script is designed to recommend movies based on a db of movies and ratings.")

import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#Fetch data and format it
data = fetch_movielens(min_rating=4.0)

#Pint training and testing data
print(repr(data['train']))
print(repr(data['test']))

#Create model
model = LightFM(loss='warp')
#Train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
    #number of users and movies in training data
    R_users, n_items = data['train'].shape
    #Generate recommendations for each user we input
    for user_id in user_ids:
            
        #movies they already like
            known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
            
            #movies our model predicts they will like
            scores = model.predict(user_id, np.arange(n_items))
            
            #rank them in order of most liked to least
            top_items = data['item_labels'][np.argsort(-scores)]
            
            #print out results
            print("User %s" %user_id)
            print("     Known positives:")
            
            for x in known_positives[:3]:
                    print("      %s" %x)
                    
            print("     Recommended:")
            
            for x in top_items[:3]:
                print("      %s" %x)
                
sample_recommendation(model, data, [3,25,450])
            
        
    