class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_hmap = {}
        for str in strs:
            hmap = Counter(str)
            master_hmap[frozenset(hmap.items())] = 0

        j = 0
        for i in master_hmap:
            master_hmap[i] = j
            j += 1

        ans = [[] for _ in range(len(master_hmap))]

        for str in strs:
            hmap = Counter(str)
            index = master_hmap[frozenset(hmap.items())]
            ans[index].append(str)
        return ans