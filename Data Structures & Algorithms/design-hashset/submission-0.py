class MyHashSet:

    def __init__(self):
    # Building empty collection of 1000 empty bins
        self.bins = [ [] for _ in range(1000)] 

    def add(self, key: int) -> None:
        # Use hash function for calculation index for bin
        binIndex = key%1000
        # Check if value input is already in any bin if not add
        if key not in self.bins[binIndex]:
            self.bins[binIndex].append(key) 

    def remove(self, key: int) -> None:
        # Find the bin and delete if it exists
        # Use hash function always
        binIndex = key%1000
        if key in self.bins[binIndex]:
            self.bins[binIndex].remove(key)

    def contains(self, key: int) -> bool:
        # Finding if value exist in bin
        binIndex = key%1000
        return key in self.bins[binIndex]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)