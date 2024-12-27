class Solution:
    def isValid(self, s: str) -> bool:
        closes = {
        ")":"(",
        "]":"[",
        "}":"{",
        }
        openingBrackets = ["(","[","{"]
        pila = list()
        for i in range(0,len(s)):
            if s[i] in openingBrackets:
                pila.append(s[i])
            elif len(pila) == 0:
                return False
            elif len(pila) > 0 and (closes[s[i]]) != pila.pop():
                return False
        if len(pila) > 0:
            return False
        return True
