#this iss direct printing
print("hello world my self dhruv@93")
#generating and save in variable
x = "dhruv"
y = "dhruv@93gmail.com"
#direct print var string
print ('Name = '+x)
#check length of string
l=len(x)
#print length of string by store in var
print (l)
#length direct print
print (len('hello this is dhruv'))
#index slice from string 
print ((y[:5])+(y[5])+(y[6:8])+(y[8:]))
#format style with place holder string concate 
print ("hi Myself {} and this is my gmail address {}".format(x,y))
#f style of formating with placeholder variable concate
print (f"{x} hi")
#uppercase and lower
print (y.upper(),x[0].upper()+x[1:].lower())
#count
print(y.count("gmail.com"))