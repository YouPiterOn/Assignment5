import random


def encrypt_formula(symbol: str, key: int, first_letter: str):
    return chr((ord(symbol) - ord(first_letter) + key) % 26 + ord(first_letter))


def decrypt_formula(symbol, key, first_letter):
    return chr(((ord(symbol) - key - ord(first_letter)) % 26 + 26) % 26 + ord(first_letter))


def f_cipher(text: str, key: int, formula):
    output = ""
    for i in range(0, len(text)):
        c = text[i]
        if c.isupper():
            c = formula(c, key, 'A')
        elif c.islower():
            c = formula(c, key, 'a')
        output += c
    return output


def encrypt(text: str, key: int):
    return f_cipher(text, key, encrypt_formula)


def decrypt(text: str, key: int):
    return f_cipher(text, key, decrypt_formula)


def normal_mode():
    inp = input("Enter text: ")
    operation = input("Chose the operation (encrypt or decrypt): ")
    key = int(input("Enter key: "))
    if operation == "encrypt":
        return encrypt(inp, key)
    elif operation == "decrypt":
        return decrypt(inp, key)


def secret_mode():
    inp = input("Enter text: ")
    key = random.randint(1, 26)
    return encrypt(inp, key)


mode = input("Chose the mode (normal or secret): ")
if mode == "normal":
    print(normal_mode())
elif mode == "secret":
    print(secret_mode())





