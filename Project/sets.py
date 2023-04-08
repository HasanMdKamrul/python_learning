# ** Unorderd, mutable , list of collection, iterable

# frogen set

frong = frozenset([2,3,4])

# frong.add(7)
# print(frong) //error dibe

setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {
    11,12,13
}

print(setA.issuperset(setB))
print(setB.issuperset(setA))
print(setB.issubset(setA))
print(setB.isdisjoint(setC))

str = set("Hello")

print(str.__len__())

str.add(1)
str.add(2)

if 1 in str:
    print("yes")

for item in str:
    print(item)

a = {
    1,2,3,4,5,6,7
}
b = {
    1,2,3,9,10,11
}

a.symmetric_difference_update(b)

print('diffup', a)

a.difference_update(b)

print(a)
diff = b.symmetric_difference(a)

print(diff)


my_set1 = {
    1,3,5,7,9
}
my_set2 = {
    0,2,4,6,8
}

primes = {
    2,5,7
}

# ** union , intersection 

print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.intersection(primes))
print(my_set2.intersection(primes))



# my_set.clear()
# my_set.add(10)
# my_set.add(12)
# my_set.add(13)

# if 16 in my_set:
#     print("yes")

# for item in my_set:
    
#     print(item)

# my_set.discard(7)
# print(my_set)

# no ordering

my_str = "hello"

my_s = set(my_str)


print(my_s)

# print(my_set)