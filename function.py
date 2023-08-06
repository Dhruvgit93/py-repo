def greeting(name,section):
    print("hello,"+ name)
    print("you are assign in "+section)

greeting("katty","ITM-A")

# calculation with  return value 
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

a=mul(36,10)
print(a)

#function calculator with multiple variable
def calculator(x,y):
    addition=x+y
    substraction=x-y
    multiplication=x*y
    division=x/y
    return addition,substraction,multiplication,division

def ans(x,y):
    a,b,c,d=calculator(x,y)
    return a,b,c,d

#print particular variable from multiple output from function
def time(d,hour,min,sec):
    day=d+hour/24+(min/60/24)+(sec/60/60/24)
    ho=(d*24)+hour+(min/60)+(sec/60/60)
    mi=(d*24*60)+(hour*60)+min+(sec/60)
    se=(d*24*60*60)+(hour*60*60)+min*60+(sec)
    return day,ho,mi,se

day,hour,min,sec=time(10,24,0,0)
print(day)


