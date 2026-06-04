class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Empty hashmap stores numbers we have already seen
        seen = {}

        # loop through and keep track of both index and item
        for i,num in enumerate(nums):
            # Calculate difference/complement
            complement = target - num
            
            # Check hashmap
            if complement in seen:
                # Return index of complement and current index
                return [seen[complement],i]
            
            # Else write current number and index in hashmap
            seen[num] = i
        # Return empty 
        return []
        