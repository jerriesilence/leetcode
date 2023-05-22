'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Solution:

        compare 2 numbers (Left, Right), from the most right, until we find the pair where the left < right;
        if there is no such pair, reverse the list as there is no "next" as "bigger"
        if there is such pair, we have located the right branch, then we are going to fint the next permutation:
            In the list starting from the Right number, find the number bigger than the Left number,
            Exchange the Left number with that number
            starting from the right number position till the end;
                sort them to get the "smallest" permutation under the NEW Left number

        '''

        if len(nums) == 1:
            return 
        elif len(nums) ==2:
            nums.reverse()
            return

        def nextOf(num,nums):
            nums.sort()
            
            i=0
            while nums[nums.index(num)+1+i] == num:
                i+=1
            return nums[nums.index(num)+1+i]
            
        for i in range(len(nums)-2+1):
            idx = -3-i
            if nums[idx+1] < nums[idx+2]:
                nextof_idx1 = nextOf(nums[idx+1], nums[idx+1:])
                nums[nums.index(nextof_idx1,idx+2)] = nums[idx+1]
                nums[idx+1]=nextof_idx1

                nums[idx+2:] =  sorted(nums[idx+2:])
                #print(nums)
                return 
            
        nums.reverse()
        #print(nums)
        return