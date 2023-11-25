# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:56:00 2023

@author: HP
"""
import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/OneDrive - MIT Academy of Engineering (MITAOE), Alandi, Pune/Desktop/ML_Acti/trained_model.sav', 'rb'))

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

