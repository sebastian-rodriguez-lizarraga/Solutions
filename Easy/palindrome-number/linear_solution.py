class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        length = len(word)
        middle = length // 2
        for i in range(0,middle):
            if word[i] != word[length-1-i]:
                return False
        return True
