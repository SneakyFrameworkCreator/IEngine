import string
import random

letters = string.ascii_letters + string.digits
rend = int(input("Enter how many passwords to generate:"))

for _ in range(rend):
    password = ''.join(random.choice(letters) for _ in range(16))
    print(password)