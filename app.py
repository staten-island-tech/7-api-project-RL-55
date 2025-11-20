def password(Email,Password):
    n=a=b=False
    if type(Email)==str and type(Password)==str:
        if "@" in Email:
            for i in Password:
                if i.isupper():
                    a=True
                elif i.isdigit():
                    b=True
                n+=1
            if a==b==True and n>=8:
                print("Account made",Email,":",Password)
            else:
                if a==0:
                    print("Password doesn't include a capital.")
                elif b==0:
                    print("Password doesn't include a number.")
                else:
                    print("Password too short.")
        else:
            print("Invalid Email type.")
    else:
        print("Email not a string.")
password("rickyl55@nycstudents.net","NathanC124")