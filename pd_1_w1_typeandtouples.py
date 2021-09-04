# x is tuple and y is list

x = ( 1, 'a', 2, 'b')
y = [ 1, 'a', 2, 'b']

# add 3.3 to list 
y.append(3.3)

# print the type
print(type(x))
print(type(y))

#print each element of list and tuple

for i in x:
    print(i)

i =0
while i < len(y):
    print(y[i])
    i +=1