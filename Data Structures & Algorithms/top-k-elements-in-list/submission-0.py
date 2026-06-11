class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We use dict to put frequencies of each num 
        counts = {}
        for num in nums:
            # We check if the current number is inside counts dict.
            # If not, we put 0
            # We always add 1 to update count
            counts[num] = counts.get(num,0) + 1

        # We create buckets array to input frequencies
        buckets = [ [] for _ in range(len(nums)+1)]

        # Map each num to bucket according to freq
        for num,freq in counts.items():
            buckets[freq].append(num)
        # Since bucket has largest frequency at the end, we walk back
        result = []
        # This causes loop to count backwards
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                # Add result value to results starting from backwards
                result.append(num)
                # if result length and k same, stop
                if len(result) == k:
                    return result
        

        