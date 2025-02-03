from random import randint

class RandomizedSet:
    """
    RandomizedSet() Initializes the RandomizedSet object.

    bool insert(int val) Inserts an item val into the set if not present. 
        Returns true if the item was not present, false otherwise.

    bool remove(int val) Removes an item val from the set if present. 
        Returns true if the item was present, false otherwise.

    int getRandom() Returns a random element from the current set of elements 
    (it's guaranteed that at least one element exists when this method is called). 
    Each element must have the same probability of being returned.
    You must implement the functions of the class such that each function works in average O(1) time complexity.
    """

    def __init__(self):
        self.values = {}

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.values[val] = 0
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        del self.values[val]
        return True

    def getRandom(self) -> int:
        keys = list(self.values.keys())
        random_i = randint(0, len(keys) - 1)

        return keys[random_i]