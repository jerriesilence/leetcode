'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = []
        res = []
        for i,c in enumerate(s):
            
            if c.lower() in ('a','e','i','o','u'):
                idx.append(i)
                res.append('')
            else:
                res.append(c)
        
        cnt = 0
        for i,c in enumerate(s):
            if c.lower() in ('a','e','i','o','u'):
                res[i] = s[idx[-1-cnt]]
                cnt += 1
        
        return ''.join(res)