class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        length = 0
        center = False
        for i in s:
            if i in hash.keys():
                hash[i] = hash[i]+1
            else :
                hash[i] = 1
        print(hash)
        for i in hash.values():
            if i%2 == 0 :
                length = length + i
            elif center == False: 
                length = length + i
                center = True
            else :
                length = length + (i-1)
            
        return length