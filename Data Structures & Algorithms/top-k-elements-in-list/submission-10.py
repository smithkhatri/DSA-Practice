class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listt = [[] for _ in range(len(nums) + 1)]
        hmap = {}
        ans = []

        for n in nums:
            if n not in hmap:
                hmap[n] = 1
            
            elif n in hmap:
                hmap[n] += 1
        
        for n, count in hmap.items():
            listt[count].append(n)
        
        
        for i in reversed(listt):
            for j in i:
                ans.append(j)
                if len(ans) == k:
                    return ans




            