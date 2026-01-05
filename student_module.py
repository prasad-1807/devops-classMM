def register(name, rollno) :
    print("Student registered")
    print(f"name: {name}")
    print(f"roll no: {rollno}")
def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successfully")
    else:
        print("Invalid credentials")
name=input()
rollno=int(input())
register(name, rollno)
login(name, rollno)