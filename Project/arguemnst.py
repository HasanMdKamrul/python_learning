# function parameters and arguments 
# ** local and global var 

def foo(num_list):
    # num = 100
    num_list= [4,5]
    num_list.append(1000)
    print(num_list)

num = 12
num_list = [2,3,4]

foo(num_list)
print(num)
    

number = 0

def my_num():
    # global number
    number = 5

my_num()

print(number)

# ** unpacking 
def funfunc(a,b,c):
    print(a+b+c)


my_list = [1,2,5]

funfunc(*my_list)

my_dict = {
    "a":2,
    "b":3,
    "c":5
}

def myfun(a,b,c):
    print(a,b,c)

myfun(**my_dict)

def my_func(a,b,c,d=100):
    print(a,b,c,d)

my_func(b=3,c=1,a=10)

# ** *args(positional arags) and **kwargs (keyword args)

def my_function(a,b,*args,**kwargs):
    print(a,b)
    # ** args is a tuple 
    for item in args:
        print(item)
    # ** kwargs is a dictionary
    for key in kwargs.keys():
        print(key,kwargs[key])
    
my_function(1,2,3,4,5,first_name="John",last_name="Doe", age=40)

my_tup = 1,2,3,4,

x = [item for item in my_tup]

print(x)


# ** force keyword args 

def fun(*args,c,d):
    for arg in args:
        print(arg)
    print(c,d)
fun(1,2,c=3,d=4)

# ** unpacking 

# args
def unpack(*args):
    for arg in args:
        print(arg)

my_list = [1,2,4,5,6]

# unpack dict

# def unpackdict(a,b,c):
#     print(a,b,c)

# my_dict = {
#     "a":1,
#     "b":2,
#     "c": 100
# }

# unpack(*my_dict)
# unpackdict(my_dict)