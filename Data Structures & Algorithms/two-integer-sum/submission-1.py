class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        """
        nums = [3,4,5,6], target = 7


        loop through nums with i

        j = target - i

        check if j existis in nums

        """
        hmap = {}
        for index_i in range(len(nums)):

            val_j = target - nums[index_i]
            
            if val_j in hmap and hmap.get(val_j, index_i) != index_i:
                return [hmap[val_j], index_i]
            
            hmap[nums[index_i]] = index_i
            






