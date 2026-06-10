class MyHashMap:

    def __init__(self):
    # Build collection of 1000 empty bins
        self.bins = [ [] for _ in range(1000)]
    
        

    def put(self, key: int, value: int) -> None:
        # Hash function
        binIndex = key % 1000
        # Loop to check if key and value exists
        for pair in self.bins[binIndex]:
            if pair[0] == key:
                pair[1] = value
                return
        # If not found, append as new pair
        self.bins[binIndex].append([key,value])

    def get(self, key: int) -> int:
        binIndex = key%1000
        # search all bins for key
        for pair in self.bins[binIndex]:
            # If key found, return value
            if pair[0] == key:
                    return pair[1]
        # This means not found
        return -1

        

    def remove(self, key: int) -> None:
        binIndex = key%1000
        # Loop to find both key and value using enumerate
        for i, pair in enumerate(self.bins[binIndex]):
            # First value of pair array is the key 
            if pair[0] == key:
                self.bins[binIndex].pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)