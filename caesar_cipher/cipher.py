import re
from caesar_cipher.corpus_loader import word_list, name_list


def encrypt(string, shift):
    
    encrypted_text = ""

    for char in string:
        print(char)
        
def decrypt():
    pass

def crack():
    pass


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass
            
    return word_count
