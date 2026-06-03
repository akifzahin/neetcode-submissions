class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        previousMap = {}
        for i,numberr in enumerate(nums):
            diff = target - numberr
            if diff in previousMap:
                return [previousMap[diff],i]
            previousMap[numberr] = i