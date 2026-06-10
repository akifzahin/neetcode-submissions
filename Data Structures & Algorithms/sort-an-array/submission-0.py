class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # if array has 0/1 elements its sorted
        if len(nums) <= 1:
            return nums
        
        # Divide and Conquer
        # 1. Divide (Find middle point and split array)
        mid = len(nums) // 2
        # Recursively call itself for left half
        leftHalf = self.sortArray(nums[:mid])
        rightHalf = self.sortArray(nums[mid:])

        # Use merge (actual sorting) function merge two arrays
        return self.merge(leftHalf, rightHalf)
    
    # Actual sorting function to sort individual arrays
    def merge(self, left:list[int], right:list[int]) -> list[int]:
        sortedList = []
        # Dual pointer method
        i = 0 # Pointer for left list
        j = 0 # Pointer for right list

        # Comparing starting element of both lists and picking smaller one
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                # Add lefts first value add to sortedList
                sortedList.append(left[i])
                # Increase i
                i+=1
            else:
                # Add rights first value add to sortedList
                sortedList.append(right[j])
                # Increase j
                j+=1
        # if any leftover values we add em
        sortedList.extend(left[i:])
        sortedList.extend(right[j:])
        return sortedList
