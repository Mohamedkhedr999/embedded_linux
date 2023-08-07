
myloginSystem = {
    "Ahmed": 1394,
    "Ali": 6078,
    "Amr": 9345
}


username = str(input("Username:"))

if username in myloginSystem:
    password = int(input("Password:"))
    if password == myloginSystem[username]:
        print("Welcome mr  "+username)
    else:
        print("Wrong password!")
else:
    print("wrong username!")
