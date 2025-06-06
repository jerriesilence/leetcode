'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        lenf = len(flowerbed)

        newly_planted = 0
        new_flowerbed = [0] * len(flowerbed) 


        for i, v in enumerate(flowerbed):     
            
            if v == 0:
                print(i)
                left = True
                right = True
                if i > 0:
                    # print(i-1)
                    # print(flowerbed[i-1])
                    if flowerbed[i-1] == 1 or new_flowerbed[i-1] == 1:
                        left = False
                if i < lenf-1:
                    if flowerbed[i+1] == 1:
                        right = False
                
                print(left)
                print(right)
                if left and right:
                    print('+1')
                    newly_planted += 1
                    new_flowerbed[i] = 1

                    if newly_planted >= n:
                        return True 
        
        return False
                
               


        