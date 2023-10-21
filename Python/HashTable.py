class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found in the hash table.")

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found in the hash table.")

# Example usage of the HashTable class
if __name__ == "__main__":
    hash_table = HashTable(size=10)
    
    # Inserting key-value pairs
    hash_table.insert("name", "Alice")
    hash_table.insert("age", 30)
    hash_table.insert("city", "New York")

    # Retrieving values
    print("Name:", hash_table.get("name"))  # Output: Alice
    print("Age:", hash_table.get("age"))    # Output: 30

    # Modifying values
    hash_table.insert("age", 31)
    print("Updated Age:", hash_table.get("age"))  # Output: 31

    # Removing a key-value pair
    hash_table.remove("city")
    try:
        print(hash_table.get("city"))  # This will raise a KeyError
    except KeyError as e:
        print(e)  # Output: Key 'city' not found in the hash table.
