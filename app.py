
def password(Email,Password):
    if "@" in Email:
        email=True
    else:
        print("Invalid Email")
    n=0
    a=2
    b=3
    c=4
    if email==True:
        for i in Password:
            if i==i.upper():
                c=True
            elif i==i.isdigit():
                b=True
            n+=1
        if n>=8:
            a=True
        if a==c==True:
            print("Account made")
        else:
            print("Invalid password")
password("rickyl55@nycstudents.net","Nathan13")