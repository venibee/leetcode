class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.rstrip(' ')
        if ' ' in x:
            start=x.rfind(' ')
            lastword=x[start:]
            k = len(lastword)-1
        else:
            k=len(x)
        return k