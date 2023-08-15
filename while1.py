import random
def main():
    range_start=1
    range_end=100
    target=random.randint(range_start,range_end)
    print("welcome to gussesing game you need to identify number between 1 to 100")
    x=0
    chance=0
    while(x!=target):
        if(chance<5):
            x=int(input("guess the number:"))
            print(target)
            y=x-target
            print(y)
            chance+=1

            if(x<1 or x>100):
                print("number is between 1 to 100")
            elif(y>=50):
                print("number is smaller, you are too far")
            elif(y>=25 and y<=49):
                print("number is smaller, you are far")
            elif(y>=10 and y<=24):
                print("number is smaller, you close")
            elif(y>=5 and y<=9):
                print("number is smaller, almost there")
            elif(y>=1 and y<=4):
                print("number is smaller, but nearest guess")
            elif(y<=-50):
                print("number is larger, you are too far")
            elif(y<=-25 and y>=-49):
                print("number is larger, you are far")
            elif(y<=-10 and y>=-24):
                print("number is larger, you close")
            elif(y<=-5 and y>=-9):
                print("number is larger, almost there")
            elif(y<=-1 and y>=-4):
                print("number is larger, but nearest guess")
            else:
                return print("congrats you win")
                break
        else:
            print("lose your chance")
            break

    
main()