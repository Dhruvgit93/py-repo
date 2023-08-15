def power(value):
    x=0
    y=0
    while(y<=value):
        print("2 ** "+str(x)+" = "+str(y))
        y=2**x
        x +=1
power(512)

