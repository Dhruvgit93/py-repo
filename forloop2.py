def sequence(n):
    list=[0,1,3,5]
    len_list=len(list)
    total=0
    for next in range(len_list,len_list+n): 
        for sum in range(0,next-1):
            total=list[sum+1]+list[sum]
            print (total)
    print(list)


sequence(5)