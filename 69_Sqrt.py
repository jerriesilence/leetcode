class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x <=3:
            return 1
        
        found = False
        lower = 0
        upper = x
            
        # binary tree
        while not found:
            i = (lower+upper)//2
            j = i + 1
            #print('-')
            #print(i)
            #print(j)
            
            if j * j < x:
                lower = i
            elif i * i > x:
                upper = i
            elif ((j * j > x ) & (i*i < x) ) :
                return i
            elif (j *j == x):
                return j
            elif (i * i ==x):
                return i
                
        
        return i
        
