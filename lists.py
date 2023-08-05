x = ['english','hindi','german']
y=['french','sanskrit']
x.insert(3,y)
print(x[2:])

from datetime import datetime
cd=datetime.now()
birth1=input(":")
birth=datetime.strftime(birth1,"%d/%m/%y")