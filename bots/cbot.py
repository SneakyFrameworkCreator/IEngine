import wikipedia
import colorama
from colorama import *
while(True):
    text = input("Enter a wikipedia article:")
    print(wikipedia.summary(text))