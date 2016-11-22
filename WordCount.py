#!/usr/bin/python
import re, string, sys

input_file_found = None
try:
    file_in_path = sys.argv[1].strip()
    # note the first argument is the 'file_name.py'
    file_in = open(file_in_path, "r")
    word_count = {}
    text_in = file_in.read().lower()
    file_in.close()
    exclude = string.punctuation + string.digits
    text_out = re.sub('['+exclude+']', '', text_in)

    for word in text_out.split():
        # note .split() splits by whitespace
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    input_file_found = True
    file_out_path = sys.argv[2].strip()
    file_out = open(file_out_path, "w")
    for key, value in word_count.items():
        print(key + " : " + str(value), file=file_out)
    file_out.close()
except FileNotFoundError:
    if input_file_found:
        print("Output file path was not found.")
    else:
        print("Input file was not found.")
