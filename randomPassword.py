import random
import string
print("welcome to random password generator")
length=int(input("enter the length for your password : "))
chars = string.ascii_letters
chars += string.digits
chars += string.punctuation
password = ""
for i in range(length):
    password += random.choice(chars)
print("so, Here is your random password: "+password)
