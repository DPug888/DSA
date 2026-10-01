#method1:
class Solution:
    def areAnagrams(self, s1, s2):
        freq1 = {}
        freq2 = {}
        for x in s1:
            freq1[x] = freq1.get(x,0)+1
        for s in s2:
            freq2[s] = freq2.get(s,0)+1
        return freq1 == freq2

#method2:
from collections import Counter
is_anagram = Counter(s1) == Counter(s2)

#method3:
is_anagram = sorted(s1) == sorted(s2)

#method4:
class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq = [0]*26
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            freq[ord(s2[i]) - ord('a')] -= 1
        return all(count == 0 for count in freq)