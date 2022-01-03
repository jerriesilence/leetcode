class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        #time limit exceeded
        n = len(s)
        if n ==0:
            result = 0
        else:
            result = 1
        
        for i in range(n):
            if n-i < result:
                return result
            for j in range(n-i):
                if j>0:
                    new_len = len(set(s[i:i+j+1]))
                    if new_len == j+1 and new_len> result:
                        result = new_len
        return result
        '''
        
        '''
        # O(n^2)
        seen = []
        maximum=0
        for i in s:
            if i in seen:
                # only count the lenth after the repeated element shows up
                maximum = max(maximum,len(seen))
                #reset the longest list by taking elements after the repeated element
                seen = seen[seen.index(i)+1:] 
            seen.append(i)
        maximum = max(maximum,len(seen))
        return maximum
        '''
        
        #O(n)
        seen = defaultdict(lambda:-1)
        cur_start = 0
        maximum=0
        for i in range(len(s)):
            if seen[s[i]]!=-1 and cur_start<=seen[s[i]]:
                maximum = max(maximum,i-cur_start)
                cur_start=seen[s[i]]+1 #new substring start after repeated element
            seen[s[i]]=i #store the index of element
        maximum = max(maximum,len(s)-cur_start)
        return maximum
