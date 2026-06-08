class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = []
        copy_strs = [0] * len(strs)

        def valid_anagram(word1, word2):
            return True if sorted(word1) == sorted(word2) else False

        for i in range(len(strs)):
            list_1 = []

            if strs[i] == "" and copy_strs[i] != -1:
                list_1.append(strs[i])

            elif copy_strs[i] != -1:
                list_1.append(strs[i])

            for j in range(i + 1, len(strs)):
                if valid_anagram(strs[i], strs[j]) and copy_strs[i] == 0:
                    list_1.append(strs[j])
                    copy_strs[j] = -1

            if len(list_1) > 0:
                ans.append(list_1)

        return ans
