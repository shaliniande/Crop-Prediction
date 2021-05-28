import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier 
from sklearn.tree import DecisionTreeClassifier
import pickle


data = pd.read_csv('E:\crop\Crop_recommendation.csv')


features = data.drop(['label'], axis=1)
target = data['label']
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.4,random_state = 2)


DecisionTree = DecisionTreeClassifier(criterion = 'entropy', max_depth = 6)
DecisionTree.fit(Xtrain,Ytrain)

#RF = RandomForestClassifier(n_estimators = 5)
#RF.fit(Xtrain,Ytrain)

pickle.dump(DecisionTree,open('crop.pkl','wb'))

