from unicodedata import name
import sys
from datetime import datetime

anglais = 'anglais'
francais = 'francais'
a = input("choose you language : anglais ou francais: ")
if a == anglais: 
    n = input("What's your name ? ")
    print("Hello", n, "nice too meet you!")
    sys.exit(print("Sorry, I have to leave I have things to do. Good bye"))
elif a == francais:
    n1 = input("Quel est votre nom ? ")
    print("Bonjours", n1, "Heureux de vous rencontrer")
    sys.exit(print("Désolé, je dois partir j'ai des choses à faire, au revoir"))
else: 
    print("I don't understand your language, Bye bye")