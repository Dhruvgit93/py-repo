# #!usr/bin/evn python
# class count:
#     num=0
#     alpa=0
# x=[]
# y=[]
# file=open("dict.py","r")
# for line in file:
#     for word in line:
#         if word.isnumeric():
#             x.append(word)
#             count.num+=1
#         if word.isalpha():
#             y.append(word)
#             count.alpa+=1
# file.close()
# print(x,y)
# print("file having {} numeric word".format(count.num))
# print("file having {} aplhabetic letter".format(count.alpa))
with open("list1.txt","w") as ls1:
    x="John Emily Michael Sarah Daniel Sophia".split()
    x.sort()
    for name in x:
        ls1.write(name+'\n')
list_1=[]
list_2=[]
with open("list2.txt","r") as ls2:
    for guest2 in ls2:
        list_2.append(guest2.strip())

with open("list1.txt","r") as ls1:
    for guest1 in ls1:
        list_1.append(guest1.strip())

guest_list=[]
guest_list=list_1+list_2
print(guest_list)
dict_guest={}
for guest in guest_list:
    if guest in dict_guest:
        dict_guest[guest]+=1
    else:
        dict_guest[guest]=1

invite_guest=[]
for guests,fre in dict_guest.items():
    if fre>1:
        print("{}: {}".format(guests,fre))
    else:
        invite_guest.append(guests)

invite_guest.sort()
print(invite_guest)
invitation_letter={}
for num_guest in invite_guest:
    invitation_letter[num_guest]="""
    hello,{}
    your invited for the celebration of company's 5th aniversary,
    we feel with joy to invite you
    """.format(num_guest)

for guest_name,letters in invitation_letter.items():
    with open("E:\py\invite\{}.txt".format(guest_name),"w") as txtletter:
        txtletter.write(guest_name+":"+letters+"\n")

# with open("invitation.txt","w") as txtletter:
#     for guest_name,letters in invitation_letter.items():
#         txtletter.write(guest_name+":"+letters+"\n")