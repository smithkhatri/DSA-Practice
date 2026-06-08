class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = []

        hmap = {}

        for word in strs:

            hmap["".join(sorted(word))] = []
        
        for word in strs:
            hmap["".join(sorted(word))].append(word)
        
        
        for key, value in hmap.items():

            answer.append(value)
        
        return answer