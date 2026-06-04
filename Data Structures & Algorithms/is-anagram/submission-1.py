class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial check of the lenght of both words (if False, then not anagram)
        if len(s) != len(t):
            return False
        # Empty dict to hold char frequencies (letter:frequency)
        counts = {}
        # Count letter in string s
        for char in s:
            # if char already in dict, add 1. Else start at 0 then add 1.
            if char in counts:
                counts[char] = counts[char] + 1
            else:
                counts[char] = 1
        # Loop through string t and subract the frequencies
        for char in t:
            # If char in not in counts/count is 0, t has character that s doesnt have.
            if char not in counts or counts[char] == 0:
                return False
            
            # Otherwise, decrease count by 1
            counts[char] -=1
        # Its an anagram if every letter is matched.
        return True
