import string
import random

def generator():
    lowercase_alphabet = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    number = '123456789'
    symbols = "{}[]()*;,_-@&.:""!#/"

    combine = uppercase_letters
    combine += lowercase_alphabet
    combine += number
    combine += symbols

    length = 15

    password = "".join(random.sample(combine, length))

    print(password)

generator()

    
