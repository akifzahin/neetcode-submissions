class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We create wall of sorting bins that sort strings to list of newly created string
        groups = collections.defaultdict(list)

        # Loop to sort characters
        for word in strs:
            # We sort chars alphabetically 
            # Sorting returns indiviual letters, we use join to make a string
            sortedWord = "".join(sorted(word))
            # Append original word to sorting bin with new sorted version
            groups[sortedWord].append(word)
        # Returns grouped lists from dict
        return list(groups.values())
        