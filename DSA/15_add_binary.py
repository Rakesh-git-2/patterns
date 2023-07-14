class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a , b = a[::-1],b[::-1]
        result = ""
        carry = 0

        for i in range(max(len(a),len(b))):
            ai = ord(a[i]) - ord("0") if i < len(a) else 0
            bi = ord(b[i]) - ord("0") if i< len(b) else 0

            total = ai + bi + carry
            char = str(total % 2)
            result = char + result 
            carry = total // 2

        if carry :
            result = "1"+result
        return result

