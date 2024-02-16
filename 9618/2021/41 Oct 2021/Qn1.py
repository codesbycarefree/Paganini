def Unknown(x,y):
    if x < y:
        print(x+y)
        return (Unknown(x+1,y)*2)
    elif x ==y:
        return 1
    else:
        print(x+y)
        Total =Unknown(x-1,y)
        half = int(Total/2)
        return half

def IterativeUnknown(x,y):
    multiply = 1
    while x!=y:
        print(x+y)
        if x<y:
            x=x+1
            multiply = multiply*2
        else:
            x=x-1
            multiply = int(multiply/2)

    return multiply

Unknown(10,15)
Unknown(10,10)
Unknown(15,10)

IterativeUnknown(10,15)
IterativeUnknown(10,10)
IterativeUnknown(15,10)