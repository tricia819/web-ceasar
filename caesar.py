from sys import argv, exit

def encrypt(text, rot):
    rot = int(rot)
    textToEncrypt = []
    textToEncrypt = list(text)

    encryptedlist = []
    encryptedtext = ""

    for char in textToEncrypt:
        encryptedchar = rotate_character(char, rot)
        encryptedlist.append(encryptedchar)
        encryptedtext = "".join(encryptedlist)
    return encryptedtext


def alphabet_position(letter):
        if letter.isupper():
            position = ord(letter) - ord("A")
        elif letter.islower():
            position = ord(letter) - ord("a")
        else:
            position = letter
        return position


def rotate_character(char, rot):
        aposition = alphabet_position(char)

        if char.isupper():
            encoded_char = (aposition + rot) % 26
            encoded_char = encoded_char + ord("A")
            encoded_char = chr(encoded_char)
            encoded_char = encoded_char.upper()

        elif char.islower():
            encoded_char = (aposition + rot) % 26
            encoded_char = encoded_char + ord("a")
            encoded_char = chr(encoded_char)
            encoded_char = encoded_char.lower()

        else:
            encoded_char = char

        return encoded_char
