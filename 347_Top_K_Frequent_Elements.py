'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        res = [0]*k
        res_count = [0]*k

        for i in nums:
            num_count[i] = num_count.get(i,0)+1
        #print(num_count)
        for num, cnt in num_count.items():
            
            #print('start')
            #print(res_count)
            for idx, c_in_res in enumerate(res_count):
                #print(f'{cnt} ? {c_in_res}')
                #print(f'idx: {idx}')
                if cnt > c_in_res:
                    res_count.insert(idx,cnt)
                    res.insert(idx,num)
                    #print(res)
                    res_count.pop(-1)
                    res.pop(-1)
                    #print(res)
                    break
                
        return res