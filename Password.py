password = "Sechaba"
count = 0
password_limit = 3
while count < password_limit:
    pas = input("Enter the password: ")
    count += 1
    if pas == password:
        print("You have successfully logged in your account")
        break
else:
    print("Sorry,your account has been blocked for 3 hours")