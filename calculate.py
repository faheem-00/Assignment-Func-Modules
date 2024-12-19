def calculate(a,o,b):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        return a/b
result=calculate(2,"+",2)
print(result)