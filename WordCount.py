#!/usr/bin/python
import re, string
try:
    user_input = input("Please type the text file path: ").strip()
    file = open(user_input, "r+")
    word_count = {}
    text_in = file.read().lower()
    exclude = string.punctuation + string.digits
    text_out = re.sub('['+exclude+']', '', text_in)

    for word in text_out.split():
        # note .split() splits by whitespace
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    for key,value in word_count.items():
        print(key + " : " + str(value))
except FileNotFoundError:
    print("File was not found.")
