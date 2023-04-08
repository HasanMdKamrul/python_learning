# ** Mutable, unorderd, "key" : "value" pair

number_dict = {
    3:9,
    2:4,
    5:25
}

first,last = 7,8,

my_dictonary = {
    "sum": first+last
}

print(my_dictonary)

print(number_dict[5])

person = {
    "name": "Hasan",
    "age" : 28,
    "Country" : "BD"
}

person3= dict(person)

person3["email"] = 'xyz@gmail.com'

print(person3)
print(person)



for key,value in person.items():
    print(key,value)

person["name"] = "kamrul"
person["email"] = "hasan@gmail.com"
# person.pop("name")
# person.popitem()

# if "email" in person:
#     print(person["email"])

try:
    print(person["email"])
except:
    print("error")

    


person2 = dict(
    name = "Era",
    age = 24,
    Country = "BD"
)

# print(person["Country"])
# print(person2["name"])

# print(person.keys())
# print(type(person))