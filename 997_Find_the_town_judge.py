class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        '''
        Count the number of people a person trust and being trusted.
        Tried Dictionary and List. List is faster than the dictionary.
        
        '''
        
        '''
        #Dictionary:
        count_trust_0 = {}
        count_trust_1 = {}
        
        for i in trust:
            count_trust_0[i[0]] = count_trust_0.get(i[0],0)+1
            count_trust_1[i[1]] = count_trust_1.get(i[1],0)+1
        
        for i in range(n):
            
            if (count_trust_0.get(i+1,0) == 0) and (count_trust_1.get(i+1,0) == n-1):
                return i+1
        
        return -1
        '''
        
        #List
        count_trust_0 = [0] * n
        count_trust_1 = [0] * n
        for a,b in trust:
            count_trust_0[a - 1] += 1
            count_trust_1[b - 1] += 1
        
        '''
        for i in range(n):
            if  count_trust_1[i] == n-1 and count_trust_0[i] == 0:
                return i + 1
        '''
        
        for i, (count0, count1) in enumerate(zip(count_trust_0,count_trust_1)):
            if count1 == n-1 and count0 == 0:
                return i+1

        return -1
            
