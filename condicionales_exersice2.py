from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE


user = "andres"
password = "andresito123"
userquestion = input("What is your user?")
passwordquestion = input("What is your password?")

if userquestion == user:
    if passwordquestion == password:
        print("Welcome to the website")
else:
    print("Access denied")

