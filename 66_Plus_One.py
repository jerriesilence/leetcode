class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # 1 digit by digit
        n = len(digits)
        i = -1
        while i >= -n and digits[i] == 9:
            digits[i] = 0
            i -= 1
            
        if i == -n-1:
            digits.insert(0,1)
        else:
            digits[i] += 1
            
        return digits
           
        '''
        # 2 transfer to number
        number = 0
        l = len(digits)
        for i in range(0,l):
            number += digits[i]*(10**(l-i-1))  
        number += 1
        digits = [int(x) for x in str(number)]  
        return digits
        '''
