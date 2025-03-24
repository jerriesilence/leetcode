class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
        """
        '''
        i = 0
        j = 0
        inserted = 0
        if m == 0:
            for idx in range(len(nums1)):
                nums1[idx] = nums2[idx]
            return
        
        if n == 0:
            return

        #print('start')
        while inserted < n:
            #print('index',i,j)
            #print('number',nums1[i], nums2[j])
            if i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
                inserted += 1
                #print('1 done, append2', nums1)
                #print(i,j,m,n)
                #print(i<m or j<n)
            elif nums1[i] < nums2[j]:
                i += 1
                print('<, move i+1')
            elif nums1[i] == nums2[j]:
                nums1.insert(i+1, nums2[j])
                nums1.pop(-1)
                m += 1
                i += 2
                j += 1
                inserted += 1
                print('=, everything +1,update: ', nums1)
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop(-1)
                i += 1
                j += 1
                m += 1
                inserted += 1
                #print('>, everything +1,update: ', nums1)
                #print(i,j,m,n)


        #print('end')
        return 
             
        '''
        # pointer from the right

        i = m-1
        j = n-1

        k = m+n-1 

        while j >=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k-=1

