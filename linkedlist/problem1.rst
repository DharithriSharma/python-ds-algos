1.  Read each line from the file (in the code) attached here, call the hash function, with size as 16.  Create a dictionary that holds the key as the hash, and value is a list associated with key. If there is a collision in the key, then the value is appended into the list. If the key does not exit, append to the dictionary.

Here is the hash function to generate a hash when a string is passed. For the size, pass 16.

def hash_string(string, size):
    return sum([ord(literal) for literal in string]) % size
the value for a given key is a list, and that list will host the word's that was hashed. It will looks like this

10: ["night", "summer", winter"]

10 is the key, which was hashed. The list contains all the words that got hashed to same key.
