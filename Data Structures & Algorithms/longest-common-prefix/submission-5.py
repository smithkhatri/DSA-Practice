class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(min(strs))
        ans = ""

        for i in range(m):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return ans
            ans = ans + (strs[j][i])
        
        return ans