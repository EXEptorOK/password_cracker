import random
import time
import os
import subprocess

def get_random_number():
    return random.randint(0, 9)

eng_alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
password_symbols = list(" !#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

def get_random_eng_letter():
    return random.choice(eng_alphabet)

def get_random_char():
    return random.choice(password_symbols)

def try_random_symbol():
    k = random.randint(0,2)
    if k == 0: return str(get_random_number())
    elif k == 1: return get_random_eng_letter()
    elif k == 2: return get_random_char()

password = input("Enter your password (8 letters)")

state = input("Use a counter of attempts? It may take more time to bruteforce(y/n)? ")
state = True if "y" else False

attempt = ""
counter = 0

print("Starting bruteforce:")

file = open("password.txt", "r")

required_time = 0
end = 0
start = time.time()

if state:
    while attempt != password and file.read() == "":
        counter += 1
        attempt = try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol()
        print(attempt)

    file = open("password.txt", "w")
    file.write("Password is:" + attempt)
    end = time.time()
    required_time = end - start
    print("Password cracked! It is: " + attempt + "\n Required time: " + required_time + "\n Attempts: " + counter)
else: 
    while attempt != password and file.read == "":
        attempt = try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol() + try_random_symbol()
        print(attempt)

    file = open("password.txt", "w")
    file.write("Password is:" + attempt)
    end = time.time()
    required_time = end - start
    print("Password cracked! It is: " + attempt + "\n Required time: " + required_time)

