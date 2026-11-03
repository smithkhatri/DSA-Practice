class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)
        
        for string in strs:
            map = [0] * 26

            for char in string:
                map[ord(char) - 97] += 1
            
            hmap[tuple(map)].append(string)
        
        return list(hmap.values())