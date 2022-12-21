# Password checker
# need to capture password using input

username = input("What is your username")
password = input("What is your password")

password_len = len(password)

hidden_pwd = '*' * password_len


print(f"{username}, your password {hidden_pwd} is {password_len} letters long")
