'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 


'''

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # t O(N)
        # s o(n)

        n_cnt = {}
        res = 0
        for n in nums:
            n_cnt[n] = n_cnt.get(n,0)+1
        
        for n in nums:
            if (2*n == k and n_cnt[n]>=2) or (2*n != k and n_cnt.get(k-n,0) >0 and n_cnt[n]>0):
                res += 1
                n_cnt[k-n] -= 1
                n_cnt[n] -= 1
        
        return res
                

        