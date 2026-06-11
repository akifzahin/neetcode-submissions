class Solution:

    def encode(self, strs: List[str]) -> str:
        # Empty string to smash all seperate ones
        res = ""
        for s in strs:
            # We attach length of string to the beginning of each string 
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # Empty structure to seperate smashed one
        res = []
        i = 0 # Walks through the smashed string char by char

        # Pointer loops until i reaches the end
        while i<len(s):
            
            # Find the '# char to read length of individual strings
            j = i # Second pointer starts from location of i
            while s[j] != "#": # While string char is not #
                j+=1 # Increment j
            
            length = int(s[i:j]) # Convert value from i to j (length of s) to integer

            i = j+1 # Negates the '#' character

            # We grab exact num of chars based on length
            word = s[i:i + length]
            res.append(word) # Add to empty structure

            i+=length # We move i to next word
        return res

