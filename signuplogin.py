Username = input("""
    Create an account
Please input Your Username: """).lower()
password = input('Input Your Password ')

print(f"User {Username} created Successfully")

loginName = input('Input Your Username ').lower()
loginPass = input('Input Your Password ')

if Username == loginName and loginPass == password:
    print('logged in Successfully')
else:
    print('Incorrect Username or password')