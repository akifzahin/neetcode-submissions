class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create empty set to store values
        seen = set()
        # Loop through each number in array
        for num in nums:
            # Check if num exists in set
            if num in seen:
                return True

            # Else we add to set and continue
            seen.add(num)
        # Return False if every value is unique and set is still empty
        return False
        