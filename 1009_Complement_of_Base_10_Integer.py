class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        result = 0
        count = 0
        if n == 0:
            return 1
        
        while n>0:
            
            digit = n % 2
            n = n//2
            new_digit = 1 - digit
            result += new_digit * (2**count)
            count +=1
        
        return result
