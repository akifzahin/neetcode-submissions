class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Three pointers to keep track of each color location
        left = 0
        right = len(nums)-1
        curr = 0

        # Condition where current doesn't exceed right
        while curr<=right:
            if nums[curr] == 0:
                # We swap current value with left value
                nums[left], nums[curr] = nums[curr], nums[left]
                # Increment pointers
                left+=1
                curr+=1
            elif nums[curr] == 2:
                # We swap current value with right value
                nums[curr], nums[right] = nums[right], nums[curr]
                # We only decrement right to move it further down the array
                # We dont change curr because we have to still inspect the values that were just swapped
                right-=1
            else:
                # Here nums[curr] == 1 so we just increment curr
                curr+=1
