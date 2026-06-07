class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        sorted_strs = sorted(strs)

        answer = ''

        for i in range(min(len(sorted_strs[0]), len(sorted_strs[-1]))):
            if sorted_strs[0][i] == sorted_strs[-1][i]:
                answer += (sorted_strs[0][i])
            else:
                break
        
        return answer