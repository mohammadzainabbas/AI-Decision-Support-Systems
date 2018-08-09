#Importing libraries
from sklearn.naive_bayes import GaussianNB
import numpy as np

#Features and their respective classes
x = np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

#Create a Gaussian classifier
model = GaussianNB()

#Train the model using training dataset
model.fit(x, y)

#Predict Output
predicted = model.predict([[1,2],[3,4]])

print(predicted)