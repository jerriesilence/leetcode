'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

class Solution(object):
    def permute(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        perm = []
        n = len(nums)

        def dfs(perm):
            #print(f'new dfs')
            #print(f'input to dfs: {perm}')
            #print(f'current res: {res}')
            #print(f'current nums: {nums}')
            
            if len(perm) == n:
                res.append(perm)
            #    print('====end of dfs====')
                return
            
            for idx,i in enumerate(nums):
            #    print(f'current i: {i}')
                nums.pop(idx)
            #    print(f'idx: {idx}')
                dfs(perm+[i])
                nums.insert(idx,i)

        dfs(perm)

        return res

            