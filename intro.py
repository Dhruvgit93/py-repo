#this iss direct printing
print ('hello world')
#generating and save in variable
x = """hii"""
yi = "dhruv"
#direct print string
print (x)

#check length of string
y=len("helllo world")

#print length of string by store in var
print(y)

#length direct print
print (len(x))

#index slice from string 
print(x[0:2].upper())

#format style with place holder string concate 
zz = 'hello,{} {}'.format(x,yi)
print(zz)

#f style of formating with placeholder variable concate
z = f'{x},{yi[0].upper()}{yi[1:]} this is your python string'
print(z)