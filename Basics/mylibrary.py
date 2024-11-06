import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#create an array start from 0 to 49
newArray=[];
for i in range(0,50):
    newArray.append(i)

empsalary=np.array(newArray)
empsalary=np.arange(50)
print(empsalary)
#find the min, max, mean from empSalary
print("Mean is",empsalary.mean())
print("Max is ",empsalary.max())
print("Min is",empsalary.min())
mydata=empsalary.reshape(5,10)
print("shape is", empsalary.shape)
print(mydata) 
print("mydata shape is", mydata.shape)
mydata=mydata+500
print(empsalary)
print(mydata>505)
