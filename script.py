import random

passLen = int(input("Enter the length of Password : "))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(s, passLen))
print(password)
