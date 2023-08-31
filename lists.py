x = ['english','hindi','german']
y=['french','sanskrit']
z=[]
z=x+y
items=""
#print(" ".join(z))
for item in z:
    items+=item+" "
print(items)
w=[1,2,3,4,5,6,7,8,9,10]
print(w[5:-1])

i=0
# Initialize a 10x10 matrix filled with zeroes
matrix = [[i] * 10 for _ in range(10)]
print (matrix)
# Printing the matrix
for row in matrix:
    print(row)
