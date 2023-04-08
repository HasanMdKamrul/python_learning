# * Error and exceptions 

# ** Self defined exceptions 

class ValueTooHighError(Exception):
    def __init__(self, message,value,*args: object) -> None:
        self.message = message 
        self.value = value
        super().__init__(*args)
class ValueTooLowError(Exception):
    def __init__(self, message,value,*args: object) -> None:
        self.message = message 
        self.value = value
        super().__init__(*args)

def valueeval(value):
    if value > 100:
        raise ValueTooHighError("Value is too high", value)
    if value < 5:
        raise ValueTooLowError("Value is too low", value)

try:
    valueeval(2)
except ValueTooHighError as e:
    print(e.message)
except ValueTooLowError as e:
    print(e.message, e.value)
    

# ** Exceptions 

try:
    x = 5/1
    z = x + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("No error found")
finally:
    print("Cleaning up ....")

# ** Syntax error 

# a = 5 print(5)

# IndexError range error 

a =  [2,3,4]

# print(a[3])

# ** Key Error

# person = {
#     "name" : "hasan"
# }

# print(person["age"])

# ** raise 

# x = -5 

# if x < 0 :
#     raise Exception("X should be greater than zero")

# ** assert 

# x = -5 

# assert (x>=0) , "Value must be greater than o or equal to zero"

# ** 