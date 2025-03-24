'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """       

        #time: O(n)
        #space: O(n) 

        n1 = len(word1)
        n2 = len(word2)
        '''
        if n1==n2:
            res = [''] * (n1*2)
            for i in range(n1):       
                res[i*2] = word1[i]
                res[i*2+1] = word2[i]

        if n1<n2:
            res = [''] * (n1*2+1)
            for i in range(n1):       
                res[i*2] = word1[i]
                res[i*2+1] = word2[i]
            
            res[2*n1] = word2[n1:]
            

        else:
            res = [''] * (n2*2+1)
            for i in range(n2):
                res[i*2] = word1[i]
                res[i*2+1] = word2[i]
            res[2*n2] = word1[n2:]
        '''
        i = 0
        res = ''
        while i < n1 or i < n2:
            if i < n1:
                res += word1[i]
            if i < n2:
                res += word2[i]

            i+=1

        return res