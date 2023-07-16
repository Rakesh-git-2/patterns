class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash = {}
        for i in magazine:
            if i in hash.keys():
                hash[i] = hash[i]+1
            else :
                hash[i] =1
        for i in ransomNote:
            if i not in hash.keys() or hash[i] < 1:
                return False
            hash[i] = hash[i]-1
        return True
