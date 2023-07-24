# by using sliding window 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            res = max(res,r-l+1)
        return res