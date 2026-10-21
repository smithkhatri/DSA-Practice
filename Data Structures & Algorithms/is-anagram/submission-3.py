class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        smap = {}
        tmap = {}

        for i in s:
            if i in smap:
                smap[i] += 1
            else:
                smap[i] = 1
        
        for j in t:
            if j in tmap:
                tmap[j] += 1
            else:
                tmap[j] = 1
        
        return smap==tmap

