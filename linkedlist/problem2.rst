2 a. Create a class

Node {
       Node next
       string word
}

in the dict, instead of pointing to a list, it will point to an object of the type Node. If hash collision occurs, then have the Node.next point to the new instance of Node object. assign the word read from the file to the word in the new object instance. Then set the current object Node's next to Nil.

b. 4 hand written diagram: First one diagram would show the first word added. The node instance shows next, word. Assume the address of the object instance is 1001, next one would be 1002. In Python object instance is always an address. Second, third and fourth diagram would show the append's to previous objects.
