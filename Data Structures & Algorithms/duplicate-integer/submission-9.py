class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        a = set(nums)

        ans = len(a) != len(nums)

        return ans