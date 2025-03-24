class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # make sure the two numbers  have the same length
        if len(a) >= len(b):
            b = '0'  * (len(a) - len(b)) + b    
        else:
            a = '0'  * (len(b) - len(a)) + a 

        result = ['0']* len(a)
        a = list(a)
        b = list(b)
        
        add_more = False

        for i in range(len(a)):
            cur = int(b[-1-i]) + int(a[-1-i])
            
            if add_more:
                cur += 1
                add_more = False

            if cur >1:
                result[-1-i] = str(cur %2)
                add_more = True
                if i == len(a)-1:
                    result = ['1'] + result
            else:
                result[-1-i] = str(cur)
        return ''.join(result)
