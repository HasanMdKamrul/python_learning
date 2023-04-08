# ** Lamda functions

# ** Lamda functions are anonymous functions

add_ten = lambda number: number+10
multi = lambda num1,num2 : num1 * num2
 
print(multi(20,10))

number2d = [
    (1,4),
    (-2,6),
    (6,6),
    (8,-2),
    (8,2),
]

sorted_numebr2D = sorted(number2d, key= lambda x: x[1] + x[0])

print(sorted_numebr2D)

# ** map --> a=[2,3,4] -> a.map((num)=> num*2) in js 

a = [2,3,4,5,6]

b = list(map(lambda x: x*2 , a))

c = [ item*2 for item in a]

print(c)
print(b)

# ** filter 

z = [ 1,2,3,4,5,6,7,8 ]

f = list(filter(lambda item: item%2 == 0, z))
t = [item for item in z if item%2 == 0]
print(f)
print(t)

# ** Reduce funct 

from functools import reduce

reduce_seq = [1,2,3,4]

result = reduce(lambda prev,current : prev+current,reduce_seq)

print(result)
