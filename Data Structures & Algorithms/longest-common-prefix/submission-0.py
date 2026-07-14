class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        solution = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            match = True

            for s in strs:
                if i == len(s) or s[i] != char:
                    match = False
                    break

            if match:
                solution += char
            else:
                break
                
        return solution