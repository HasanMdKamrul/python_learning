from collections import Counter, OrderedDict, defaultdict, deque, namedtuple

de = deque()


de.append(4)
de.append(4)
de.append(7)
de.appendleft(2)
de.popleft()

print(de)

d = defaultdict(list)

d['a'] = 1
d['b'] = 2

print(d["z"])


orderd_dict = {}


orderd_dict['b'] = 2
orderd_dict['c'] = 3
orderd_dict['d'] = 4
orderd_dict['a'] = 1

print(orderd_dict)

# * creating a class 

Point = namedtuple('Point',"x,y")
# make instance 
pt = Point(4,-8)

print(pt.x)
print(pt.y)

a = [1,2,4,5,6,73,2,1]

my_counter = Counter(a)

print(my_counter)

# for i in my_counter.values():
#     print(i)

# print(my_counter.most_common()[0][1])

