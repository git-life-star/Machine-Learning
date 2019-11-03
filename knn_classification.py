import random
import math
# Reading the data file without using pandas
a=open("/home/deeksha/Downloads/iris.data")
list2=[]
for i1 in a:
    we=i1.split(',')
    we[0]=float(we[0])
    we[1]=float(we[1])
    we[2]=float(we[2])
    we[3]=float(we[3])
    we[4]=we[4][:-2]
    list2.append(we)
# Splitting into training and test data
def train_test_split(data,training_data,test_data,split=0.75):
    for i1 in data:
        if (random.random()<split):
            training_data.append(i1)
        else:
            test_data.append(i1)
# Euclidean Distance(Parameter single data)
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
        final.append(you[i][1])
    return final
# Finding majority of votes
def predict_class_label(final):
    d=dict()
    for i in range(0,len(final)):
        a1=final[i][4]
        d[a1]=d.get(a1,0)+1
    b=max(list(d.values()))
    for i in d:
        if (d[i]==b):
            return i
# Driver Program
training_data=[]
test_data=[]
train_test_split(list2,training_data,test_data)
# Predicting the label of test_data
print(len(training_data))
print(len(test_data))
for i in test_data:
    final=nearest_neighbour(training_data,i,3)
    ans=predict_class_label(final)
    print("Predicted Value",ans)
    print("Actual Value",i[4])
    print("")








