class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 201
        min_word = ""
        for word in strs:
            length = len(word)
            if length < min_length:
                min_length = length
                min_word = word
        ans = ""
        for i in range(0,min_length):
            valid_letter = True
            for word in strs:
                valid_letter &= min_word[i] == word[i]
            if valid_letter:
                ans = ans + min_word[i]
            else:
                break
        return ans

            
