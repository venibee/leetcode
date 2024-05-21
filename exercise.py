class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.rstrip(' ')
        if ' ' in x:
            start=x.rfind(' ')
            lastword=x[start+1:]
            k = len(lastword)
        else:
            k=len(x)
        return k
    def second(self, s):
        return len(s.split(" ")[-1])