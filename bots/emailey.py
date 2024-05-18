import string
import random
from colorama import *
import colorama
colors = [Fore.GREEN,Fore.RED,Fore.BLUE,Fore.YELLOW]
letters = string.ascii_letters + string.digits
rend = int(input("Enter how many passwords to generate: "))
ending = input("Enter ending without @: ")

for _ in range(rend):
    password = random.choice(colors) + ''.join(random.choice(letters) for _ in range(16)) + '@' + ending
    print(password)