'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''

# Recursive
class Solution(object):
    def numDecodings(self, s): 
        """
        :type s: str
        :rtype: int
        """
        
        # recursive base case
        if s[0] == '0':
            return 0
        elif int(s) <= 10 or int(s) == 20:
            return 1
        elif int(s) <=26:
            return 2
        # revursive cases
        ## get the strings into half, and solve the problem recursively using the first and second half of the string
        ## example: f(111111) = f(111) * f(111) + f(11) * f(11) * bool(11 belongs to 26 charactors)
        ## example: f(113111) = f(113) * f(111) + f(11) * f(11) * bool(31 belongs to 26 charactors)
        elif len(s)<=3:
            if int(s[:2]) <= 26 and s[1] != '0':
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            elif int(s[:2]) == 10 or int(s[:2]) == 20:
                return self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])
        else:
            n = len(s)
            mid = int(n/2)
            if int(s[(mid-1):(mid+1)]) <= 26 and int(s[(mid-1)]) != 0:
                return self.numDecodings(s[:mid])*self.numDecodings(s[mid:]) + self.numDecodings(s[:(mid-1)]) * self.numDecodings(s[(mid+1):]) 
            else:
                return self.numDecodings(s[:mid])*self.numDecodings(s[mid:])

# Dynamic Programing             
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        dp[0] = 1

        if s[0] == '0':
            return 0

        else:
            dp[1] = 1
        
        for i in range(1,len(s)):
            if int(s[i]) > 0:
                dp[i+1] += dp[i]
            
            if 10 <= int(s[(i-1):(i+1)]) and  int(s[(i-1):(i+1)]) <=26:
                dp[i+1] += dp[i-1]

        return dp[-1]
