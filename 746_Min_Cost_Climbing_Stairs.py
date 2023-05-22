'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        '''
        cost = [10,15,20]

        s-2: s = 0
        s-1: s = 0    
        s0: s = 10        -> cost = min(s-1 + c0, s-2 + c0)
        s1: s = 15        -> cost = min(s0 + c1, s-1 + c1)
        s2: s = 30        -> cost = min(s1 + c2, s0 + c2)
        s3: s = 15        -> cost = min(s2 + c3, s1 + c3)
        '''

        c_m = 0
        c_n = 0

        cost.append(0)
        
        for i in cost:
            if c_m + i < c_n + i:
                c_i = c_m + i
            else:
                c_i = c_n + i
            c_m = c_n
            c_n = c_i
        
        return c_i