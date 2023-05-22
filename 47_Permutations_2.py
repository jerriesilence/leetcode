'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 '''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        each_permutation = []
        num_counts = {}

        for i in nums:
            num_counts[i] = num_counts.get(i,0) + 1

        
        def dfs():

            if len(each_permutation) == len(nums):
                res.append(each_permutation.copy()) #.copy python 3 only
            
            for n in num_counts:
                if num_counts[n] > 0:
                    each_permutation.append(n)
                    num_counts[n] -= 1
                    dfs()
                    num_counts[n] += 1
                    each_permutation.pop(-1)
        
        dfs()
                    
        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        n = len(nums)
        
        num_counts = {}

        for i in nums:
            num_counts[i] = num_counts.get(i,0) + 1

        def dfs(perm):
            #print(f'new dfs')
            #print(f'input to dfs: {perm}')
            #print(f'current res: {res}')
            #print(f'current nums: {nums}')
            
            if len(perm) == n:
                res.append(perm)
            #    print('====end of dfs====')
                return
            
            for i,count in num_counts.items():
            #    print(f'current i: {i}')
                if count>0:
                    num_counts[i] -= 1
            #    print(f'idx: {idx}')
                    dfs(perm+[i])
                    num_counts[i] += 1

        dfs(perm)

        return res