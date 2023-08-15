def round(number):
    x=10
    fd=number//10
    reminder=number%10
    round_down=fd*10
    round_up=(fd+1)*10
    if reminder < 5:
        return (round_down)
    else :
        return(round_up)

print(round(371))