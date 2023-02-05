def hash_string(string, size):
    return sum([ord(literal) for literal in string]) % size

class Node:
    def __init__(self, word):
        self.word = word
        self.next = None

def read_file(file_name, size):
    hash_dict = {}
    with open(file_name, 'r') as f:
        for line in f:
            word = line.strip()
            h = hash_string(word, size)
            new_node = Node(word)
            if h in hash_dict:
                current_node = hash_dict[h]
                while current_node.next is not None:
                    current_node = current_node.next
                current_node.next = new_node
            else:
                hash_dict[h] = new_node
    return hash_dict

file_name = "file.txt"
size=16
hash_dict = read_file(file_name, 16)
print(hash_dict)