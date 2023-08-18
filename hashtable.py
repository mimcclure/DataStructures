#allows for quick insertion, deletion, and retrieval of data. Hash function that maps keys to indices

#implementation
#represent node in a linked list
class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

#contain the array that will hold the linked list
class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    #hash method takes the key and returns the index in the array where the key-value pair should be stored. Python has a built-in hash function to hash the key and then use modulo to get an index in the array
    def _hash(self, key): 
        return hash(key) % self.capacity

    #insert key value pair. Takes index where the pair should be stored using the hash method and if no linked list is at that index, it creates a new node and sets it as the head of the list. Iterate through the list until the last node is found or the key alr exists, and update the value if it does.
    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    #search method retrieves the value associated with a given key. Gets the index where the key-value pair should be using the hash method then searches the list at that index for the key. Returns the key if it's found, raises a KeyError if it isn't.
    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)
    
    #remove method. Similar logic to search, but the key node gets removed from the list. Raises a KeyError if it doesn't find a key.
    def remove(self, key):
        index = self._hash(key)

        prev = None
        current = self.table[index]

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

        return KeyError(key)
    
    #string representation
    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)
