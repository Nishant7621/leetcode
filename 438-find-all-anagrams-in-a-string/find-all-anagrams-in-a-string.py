class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        m = len(p)

        if m > len(s):
            return res

        target = sorted(p)

        for i in range(len(s) - m + 1):
            if sorted(s[i:i + m]) == target:
                res.append(i)

        return res