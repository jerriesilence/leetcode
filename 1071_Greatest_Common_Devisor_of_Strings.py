'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.


'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        '''
        Complexity Analysis
Let m,nm, nm,n be the lengths of the two input strings str1 and str2.

Time complexity: O(min⁡(m,n)⋅(m+n))O(\min(m, n) \cdot (m + n))O(min(m,n)⋅(m+n))
We checked every prefix string base of the shorter string among str1 and str2, and verify if both strings 
are made by multiples of base.
There are up to min⁡(m,n)\min(m, n)min(m,n) prefix strings to verify and each check involves iterating over 
the two input strings to check if the current base is the GCD string, which costs O(m+n)O(m + n)O(m+n). 
Therefore, the overall time complexity is O(min⁡(m,n)⋅(m+n))O(\min(m, n) \cdot (m + n))O(min(m,n)⋅(m+n)).

Space complexity: O(min⁡(m,n))O(\min(m, n))O(min(m,n))
We need to keep a copy of base in each iteration, which takes O(min⁡(m,n))O(\min(m, n))O(min(m,n)) space.
        '''
        
        #start with base= str1

        # check if both str1 & str2 are made of base:
          # if yes: return base
          # if no:  remove last character from base, do that again until find base or return empty
        len1, len2 = len(str1), len(str2)
        if len1 <= len2:
            base = str1
        else:
            base = str2

        def find_base(base):
            if base == "":
                return False

            n = len(base)
            if len1 % n == 0 and len2 % n == 0:
                n1 = len1/n
                n2 = len2/n

                if n1*base == str1 and n2*base == str2:
                    return True

            return False

        while len(base) > 0:
            if find_base(base):
                return base
            else: 
                base = base[:-1]

        return ''
        
        