class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        # for i in nums:

        #     check if i is in hmap
        #     if it is then, return false

        #     save i to hmap

        # return true


        hmap = {}

        for i in nums:

            if i in hmap:
                return True
            
            hmap[i] = 0

        
        return False
            