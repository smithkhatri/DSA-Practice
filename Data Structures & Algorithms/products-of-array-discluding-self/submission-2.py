class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # out = [0 for _ in range(len(nums))]
        out = []
        left = []
        right = []
        l = 1

        for i in nums:
            l = i*l
            left.append(l)
        
        r = 1

        for i in reversed(nums):
            r = i*r
            right.append(r)
        
        right = list(reversed(right))

        out.append(right[1])

        for i in range(1, len(nums)-1):
            out.append(left[i-1] * right[i+1])
        
        out.append(left[-2])

        return out