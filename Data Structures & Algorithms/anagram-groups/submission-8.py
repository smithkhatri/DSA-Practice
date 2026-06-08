class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        def asc_value(word):
            asc_map = ["0"] * 26

            for letter in word:
                asc_map[ord(letter) - ord("a")] += "1"

            return asc_map

        for word in strs:
            hmap["".join(asc_value(word))].append(word)
        
        return list(hmap.values())


