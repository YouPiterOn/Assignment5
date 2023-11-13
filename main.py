def encrypt_formula(symbol, key, first_letter):
    return (symbol - ord(first_letter) + key) % 26 + ord(first_letter)


def decrypt_formula(symbol, key, first_letter):
    return (symbol - ord(first_letter) + key) % 26 + ord(first_letter)


def f_cipher(text, key, formula):
    output = ""
    for i in range(0, len(text)):
        c = text[0]
        if c.isupper():
            c = formula(c, key, 'A')
        elif c.islower():
            c = formula(c, key, 'a')
        output += c
    return output


def encrypt(text, key):
    return f_cipher(text, key, encrypt_formula)


def decrypt(text, key):
    return f_cipher(text, key, decrypt_formula)

