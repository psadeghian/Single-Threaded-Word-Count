#!/usr/bin/python
try:
    user_input = input("Please type the text file path: ").strip()
    file=open(user_input,"r+")
    word_count = {}
    for word in file.read().split():
        # note .split() splits by whitespace
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    for key,value in word_count.items():
        print(key + " : " + value)
except FileNotFoundError:
    print("File was not found.")
