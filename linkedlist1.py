import os

def hash_string(string, size):
    return sum([ord(literal) for literal in string]) % size

def read_file(file_name, size):

    dict = {}

    with open(file_name, "r") as f:

        for line in f:

            h = hash_string(line.strip(), size)

            if h in dict:

                dict[h].append(line.strip())
            else:

              dict[h] = [line.strip()]
    return dict
file_name = "file.txt"
size = 16
dict = read_file(file_name, size)
print(dict)