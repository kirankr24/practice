import csv 

#covert dist into list 
# with statement in Python is used in exception handling to make the code cleaner 
# and much more readable. It simplifies the management of common resources like file streams.
with open("mpg.csv") as datacsv:
    data = list(csv.DictReader(datacsv)) 

print(data[0])

#length 
print(len(data))

print("------------------------------------------")

print(data[0].keys())

print("------------------------------------------")
# average    
x = sum(float(d['cty']) for d in data)/len(data)
print(round(float(x),2))

print("------------------------------------------")
# total available cylinders

cylinders = set(d['cyl'] for d in data)
cylinders = sorted(cylinders)
ctydatabycyl = []


for c in cylinders:
    sumdata = 0
    cyltypeconut = 0
    for d in data:
        if d['cyl'] == c:
            sumdata += float(d['cty'])
            cyltypeconut +=  1
    ctydatabycyl.append((c, round(sumdata/cyltypeconut,2)))


data1 = ctydatabycyl.sort(key=lambda x:x[0])
print(ctydatabycyl)

print("---------------------------------------------------------")

vehicle = sorted(set(d['class'] for d in data))
hvybycls = []

for c in vehicle:
    sumd = 0
    vclssd = 0
    for d in data:
        if d['class'] == c:
            sumd += float(d['hwy'])
            vclssd += 1 

    hvybycls.append((c, round(sumd/vclssd,2)))

hvybycls.sort(key = lambda x:x[0])

print(hvybycls)