def letter(name,address,salary):
    print("""to,
    mr.{},
    {}
    dear {},
    this is to inform you that you are selected for this job,
    congratulation.
    annual salary {:.2f}/-
    bonus {:.2f}/-
    """.format(name,address,name,salary,(salary/10)/2))

names=['jay','henil','fenil']
addresses=['5,Ram nagar,Amreli','street-16,Batar,Surat','Central London,UK']
salarys=[250000,500000,700000]
x=len(names)
print (x)
for letters in range(0,x):
    letter(names[letters],addresses[letters],salarys[letters])


def check(sentence,old):
    print (old)
    if check(sentence[0],old):
        sentence[0]=sentence[0].replace(".html",".h")
    print(sentence[0])

check(["hello hy jack.html jack jack jack"],"jack")