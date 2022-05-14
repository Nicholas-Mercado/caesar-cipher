import re
from caesar_cipher.corpus_loader import word_list, name_list


def encrypt(string, shift):

    encrypted_text = ""

    lower_offset = 97
    upper_offset = 65

    for char in string:

        if char.isalpha():
            if char.islower():
                char = chr((ord(char) + shift - lower_offset) %
                           26 + lower_offset)
                encrypted_text += char
            if char.isupper():
                char = chr((ord(char) + shift - upper_offset) %
                           26 + upper_offset)
                encrypted_text += char
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def crack(string):
    for i in range(26):
        cracked_string = decrypt(string, i)
        word_count = count_words(cracked_string)
        decimal = int(word_count / len(string.split()))
        if decimal > .5:
            return cracked_string

    return


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+', '', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass

    return word_count
