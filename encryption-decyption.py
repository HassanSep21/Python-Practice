
import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
random.shuffle(key)

# encyption

plain_txt = input("Enter yout text: ")
cypher_txt = ""

for letter in plain_txt:
    index = char.index(letter)
    cypher_txt += key[index]

print(f"Encrypted text: {cypher_txt}")

# decryption

cypher_txt = input("Enter yout cypher text: ")
plain_txt = ""

for letter in cypher_txt:
    index = key.index(letter)
    plain_txt += char[index]

print(f"Decrypted text: {plain_txt}")