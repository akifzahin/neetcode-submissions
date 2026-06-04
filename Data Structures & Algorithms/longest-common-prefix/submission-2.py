class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If input empty, return empty
        if not strs:
            return ""
        
        # We take our first word as base for prefix
        firstWord = strs[0]

        # Loop each character of first word vertically
        for i, char in enumerate(firstWord):
            # Check character against all other words (starting from index 1)
            for otherWord in strs[1:]:
                # Check if running out of letters or chars don't match
                if i == len(otherWord) or otherWord[i] != char:
                    # Returns firstWord before current index
                    return firstWord[:i]
        # If loop finishes, entire first word is common prefix
        return firstWord
