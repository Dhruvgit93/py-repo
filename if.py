def minchar(email):
    if len(email)>13:
        if (email[-10:].lower()=="@gmail.com"):
            print(email[-10:].lower())
            return "valid gmail address"
        return "@gmail.com is not correct"
    return  "minimum 3 character before @gmail.com"

print(minchar("dhruv@gmail.com"))

