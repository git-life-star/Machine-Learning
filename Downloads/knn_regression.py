# Implementing knn Regression from scratch
import random
import math
import pandas as pd
import numpy as np
print(1)
df=pd.read_csv("/home/deeksha/Downloads/diamonds1.csv")
# Preprocessing of data
# Convert categorical data to numerical data
cut_dict={"Ideal":1,"Good":2,"Premium":3,"Very Good":4,"Fair":5}
color_dict={"E":1,"I":2,"J":3,"H":4,"F":5,"G":6,"D":7}
clarity_dict={"SI2":1,"SI1":2,"VS1":3,"VS2":4,"VVS2":5,"VVS1":6,"I1":7,"IF":8}
df["cut"]=df["cut"].map(cut_dict)
df["color"]=df["color"].map(color_dict)
df["clarity"]=df["clarity"].map(clarity_dict)
print(df)
# Directly edited CSV File for Unnamed Index:0
# Splitting the data into training and test sets
df=df.iloc[:150]
msk=np.random.rand(len(df))<0.8
train=df[msk]
#train=train.reset_index()
#print(train)
test=df[~msk]
#print(train.iloc[3])
# Calculating euclidean distance
#def euclidean_distance(data_instance1,data_instance2):
 #   distance=0
test_data=[]
train_data=[]
for i in range(0,len(test)):
    we=[]
    for col in test:
        if col!="price":
            we.append(test.iloc[i][col])
    we.append(test.iloc[i]["price"])
    test_data.append(we)
for i in range(0,len(train)):
    me=[]
    for col in train:
        if col!="price":
            me.append(train.iloc[i][col])
    me.append(train.iloc[i]["price"])
    train_data.append(me)
def euclidean_distance(data_instance1,data_instance2):
    distance=0
    for i in range(0,4):
        distance+=pow(data_instance1[i]-data_instance2[i],2)
    return math.sqrt(distance)
# Finding k nearest neighbour
def nearest_neighbour(training_data,test_data_instance,k):
    you=[]
    for i in training_data:
        dis=euclidean_distance(i,test_data_instance)
        you.append((dis,i))
    you.sort()
    final=[]
    for i in range(0,k):
        final.append(you[i][1][9])
    return final
# Finding the predicted continuous value
predict=[]
actual=[]
def predict_value(final):
    predictvalue=0
    for i in range(0,len(final)):
        predictvalue+=final[i]
    predictvalue=predictvalue/len(final)
    return predictvalue
for i in test_data:
    final=nearest_neighbour(train_data,i,3)
    ans=predict_value(final)
    print("Predicted Value",ans)
    print("Actual Value",i[9])
    predict.append(ans)
    actual.append(i[9])
    print("")


