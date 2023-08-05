def greeting(name,section):
    print("hello,"+ name)
    print("you are assign in "+section)

greeting("katty","ITM-A")

# calculation
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

a=mul(36,10)
print(a)

def time(hour,min,sec):
    second=hour*60*60 + min*60 +sec
    minute=hour*60+min
    day=hour/24
    return second,minute,day


second,minute=time(12,10,30)
print(second,minute,day)


