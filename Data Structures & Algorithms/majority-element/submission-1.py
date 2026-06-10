class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        from collections import defaultdict

        hmap = defaultdict(int)
        
        for num in nums:

            hmap[num] += 1

            if hmap[num] > len(nums)/2:
                return num
        
        