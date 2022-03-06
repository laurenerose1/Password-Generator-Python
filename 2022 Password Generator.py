## simple password generator using upper and lowercase characters, digits, symbols and the random library.
import random #import library , also note there are more secure modules over random

#potential characters, digits and symbols for password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower() #same content as above but lowercase so we dont duplicate
digits = "0123456789"
symbols = "()[]{},;:.-_/+*#!? "

upper, lower, nums, syms = True, True, True, True #uppercase, lowercase, numbers and symbols will be potential outputs if marked true

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

print("\n Looking for some password inspiration? We can help! Below are some super strong password options ->>>> : \n")
length = 20 #length of password
amount = 10  # number of passwords to generate right now

for x in range(amount):
    password = "".join(random.sample(all, length)) #will take random sample out of full string
    print(password) 