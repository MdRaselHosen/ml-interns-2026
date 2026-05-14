
def summ(a,b):
    return a+b

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Division by zero is not allowed"
    return a/b 

def power(a,b):
    return a**b


print(summ(3,4))
print(minus(10,5))
print(multi(3,4))
print(div(4,3))
print(power(3,4))