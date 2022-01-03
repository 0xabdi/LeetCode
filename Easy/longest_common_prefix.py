class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

        Input: strs = ["dog","racecar","car"]
        Output: ""

        Algorithm
        1. Check if the string array is empty
            1.1 If empty, return empty string (i.e. "")
        2. Get the lenght of the shortest string
        3. Declare an empty string
        4. Iterate from 0 to minlen
            4.1 
        """

        if len(strs) == 0:
            return ""

        min_len = len(strs[0])

        for i in range(1, len(strs)):
            min_len = min(min_len, len(strs[i]))

        longest_prefix = ""

        for i in range(min_len):
            first_letter = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != first_letter:
                    return longest_prefix
            longest_prefix += first_letter
        
        return longest_prefix



