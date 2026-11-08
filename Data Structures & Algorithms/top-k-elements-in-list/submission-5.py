class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = set()
        hmap = {}
        out = []

        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            if n not in seen: # Did we see n? No: continue, Yes: move on
                hmap[n] = 1
                seen.add(n)
            
            elif n in seen:
                hmap[n] += 1

        for n, count in hmap.items():
            bucket[count].append(n)
        
        c = 0




        for i in reversed(bucket):
            for j in i:
                out.append(j)
                c = c + 1
                if len(out) == k:
                    return out
