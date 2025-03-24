'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        '''
        ############## t O(n) s O(n) ##############
        prod_left = 1
        left = [1]
        prod_right = 1
        right = [1]
        for i,v in enumerate(nums):
            prod_left *= v
            left.append(prod_left)

            prod_right *= nums[-1-i]
            right.append(prod_right)
        #print(left,right)
        # nums[i] prod on the left is left[i], ignoring left[-1]
        # nums[i] prod on the right is right[-2-i], ignoring right[-1]
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[-2-i])
        '''

        #        1,  2,  3, 4
        #l:      1,  1,  2, 6,24
        #r: 24  24, 12,  4, 1
    #r(order)    4, 12, 24, 24
        #res:   24, 12,  8, 6
        #

        ############### t O(n) s O(1) ##############
        prod_left = 1
        ans = [0] * (len(nums)+1)
        ans[0] = 1

        for i,v in enumerate(nums):
            ans[i+1] = ans[i] * v 

        r = 1
        for i,v in enumerate(nums):
            if i<len(nums)-1:
                r = r * nums[-1-i]
                ans[-3-i] = ans[-3-i] * r

        #print(left,right)
        # nums[i] prod on the left is left[i], ignoring left[-1]
        # nums[i] prod on the right is right[-2-i], ignoring right[-1]

        return ans[:-1]



        

# solution of s o(1):
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
