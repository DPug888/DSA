class Solution:
    def firstRepChar(self, s):
        freq = {}
        for x in s:
            if x in freq:
                return x
            freq[x] = 1
        return "-1"