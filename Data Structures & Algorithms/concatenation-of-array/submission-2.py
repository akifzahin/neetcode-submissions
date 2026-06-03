class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # Length of original array
        n = len(nums)
        # Initialize ans with 2 times the size of n
        ans = [0]*(2*n)
        # Loop only once
        for i in range(n):
            ans[i] = nums[i] # Enter at i place
            ans[i+n] = nums[i] # Enter at offset by length
        return ans