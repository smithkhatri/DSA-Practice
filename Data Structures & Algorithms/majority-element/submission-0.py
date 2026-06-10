class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        from collections import defaultdict

        hmap = defaultdict(int)
        
        for num in nums:

            hmap[num] += 1
        
        for key, value in hmap.items():

            if value > len(nums)/2:
                return key

