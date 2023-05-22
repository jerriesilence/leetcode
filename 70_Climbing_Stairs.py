'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. 
        In how many distinct ways can you climb to the top?
        """

        '''
        n = 1: 1                                  -> 1
        n = 2: 1+1; 2                             -> 2
        n = 3: 1+1+1; 2+1; 1+2                    -> 3 = f(2) + f(1)
        n = 4: 1+1+1+1; 2+1+1; 1+2+1; 1+1+2; 2+2  -> 5 = f(3) + f(2)
        '''
        c_m = 1
        c_n = 1

        if n == 1:
            return 1

        for i in range(n-1):
            c_i = c_m + c_n
            c_m = c_n
            c_n = c_i   

        return c_i   