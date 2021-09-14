import csv 
import math

#covert dist into list 
# with statement in Python is used in exception handling to make the code cleaner 
# and much more readable. It simplifies the management of common resources like file streams.
with open("data.csv") as datacsv:
    data = list(csv.DictReader(datacsv)) 

print(data[:3])

#length 
print(len(data))

print("------------------------")

print(data[0].keys())

print("------------------------")
# average    
x = sum(float(d['cty']) for d in data)/len(data)
print(round(float(x),2))

print("------------------------")
# total available cyclinders

cylinders = set(float(d['cyl']) for d in data)

cyldatatype = []


for c in cylinders:
    sumdata = 0
    cyltypeconut = 0
    for d in data:
        if d['cyl'] == c :
            sumdata = sumdata + float(d['cty'])
            cyltypeconut = cyltypeconut +  1

    cyldatatype.append(c, sumdata/cyltypeconut)


data1 = cyldatatype.sort(key=lambda x:x[0])
print(data1)