# in this file we discussed class map and lambda
# std coding for class in python

#use camel style to create class name

class Person:
    department = 'School of Information'

    def self_name(self, new_name):
        self.name = new_name
    
    def self_location(self, new_location) :
        self.location = new_location

person = Person()
person.self_name('Kiran Kumar Chaudhary')
person.self_location('Gujarat, India')
print("My name is {} and i'm currently living in {} and study in {}".format(person.name, person.location,person.department))

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.35, 2.01]

cheapest = map(min, store1, store2)
print(cheapest)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 
'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
        title = person.split()[0]
        lastname = person.split()[-1]
        return "{} {}".format(title, lastname)


print(list(map(split_title_and_name, people)))

print("=============Lambda starts here==================")

my_function = lambda a,b,c : a+b
print(my_function(1,2,3))


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
my_lambda = lambda person : person.split()[0]+ '' + person.split()[-1]
for person in people:
    print(my_lambda(person))


for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
print(list(map(my_lambda, people))) 

print(list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))

print("=============Lists starts here==================")

my_list =[]

for d in range(0,100):
    if d%2 == 0:
        my_list.append(d)

print(my_list)

print("=============Shortcut==================")
# short code
my_list = []

my_list= [d for d in range(100) if d%2 == 0]
print(my_list)