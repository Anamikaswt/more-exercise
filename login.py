print("login or signin")
login=input("enter 1 for sign up and enter 2 for login ")
if login=="1":
    user=input("enter your name")
    file1=open("login.txt","r")
    a=file1.read()
    if user in a:
        print("user already exist")
    else:
        password=input("creat the password")
        b=open("login.txt","a")

        
