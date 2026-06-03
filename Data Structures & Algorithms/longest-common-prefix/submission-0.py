class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    #if list empty no prefix
        if not strs:
            return ""
        
        #pick first word as our reference
        first_word = strs[0]

        #go through first word letter by letter
        for i in range(len(first_word)):

            #grab char at current position
            char = first_word[i]

            #loop to check every other word in list
            for j in range(1,len(strs)):
                #stop only if i is equal length of current word
                #i is not same as char
                if i ==len(strs[j]) or strs[j][i] != char:
                    #if not match, then return word until i
                    return first_word[:i]
        #if the outerloop finished without stopping, then itself is prefix.
        return first_word
