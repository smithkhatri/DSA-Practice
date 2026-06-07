class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest_string = min(strs, key=len)
        answer = ''
        c = 0

        print(smallest_string)

        
        

        for i in range(len(strs)):
            for j in range(len(smallest_string)):
                
                
                
                if strs[i][j] == smallest_string[j] and c==j:
                    answer += (strs[i][j])
                    c += 1
                
                
            smallest_string = answer
            answer = ''
            c = 0
        
        return smallest_string