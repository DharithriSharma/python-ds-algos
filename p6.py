class Node:
    def _init_(self, word, next=None):
        self.word = word
        self.next = next

def hash_string(string, size):
    return sum([ord(literal) for literal in string]) % size


def read_file(filepath, size):
    hash_dict = {}
    with open(filepath, "r") as file:
        for line in file:
            word = line.strip()
            hash_val = hash_string(word, size)
            if hash_val in hash_dict:
                new_node = Node(word, hash_dict[hash_val])
                hash_dict[hash_val] = new_node
            else:
                new_node = Node(word)
                hash_dict[hash_val] = new_node
    return hash_dict

file_name = "file.txt"
size=16
hash_dict = read_file(file_name,16)