class LoginError(Exception):
    pass
USERNAME = "admin"
PASSWORD = "1234"

try:
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    if username != USERNAME or password != PASSWORD:
        raise LoginError("Error : Invalid Username or Password.")
    print("Login Sucessfull")
except LoginError as e:
    print(e)
