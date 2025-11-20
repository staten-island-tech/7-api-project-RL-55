def password(Email,Password):
    if type(Email)!=str and type(Password)!=str: return("Email or password not a string.")
    if "@" not in Email: return("Invalid Email type.")
    if not any (i.isupper for i in Password): return("Password doesn't include a capital.")
    if not any (i.isdigit for i in Password): return("Password doesn't include a number.")
    if not len(Password)>=8: return("Password too short.")
    return("Account made",f"Your Email:{Email} and Password:{Password}")
print(password("rickyl55@nycstudents.net","NathanC"))