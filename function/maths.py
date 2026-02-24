# Simple Math
# Write four functions — add, subtract, multiply, divide — each taking two numbers and returning the result. For divide, handle division by zero.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a,b):
    return  a*b

def div(a,b):
    if a==0:
        print("Can not divide 0")
    elif b==0:
        print("Can not divide 0")
    else:
     return a/b

a = int(input("Enter first mumber:"))
b = int(input("Enter second number:"))

print("Addition:", add(a,b))
print("Subtraction:", sub(a,b))
print("Multiply",mul(a,b))
print("Divide",div(a,b))



