class Solution(object):
    def uniquePaths(self, m, n):
        """
        There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

        Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner. 
        :type m: int
        :type n: int
        :rtype: int
        """


        # dfs recursive:

        #if m == 1 or n == 1:
        #    return 1

        #return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)

        # DP: first row and first col will always be 1; following recursive..

        # set up matrix:
        dp = [[1] * n] * m
        #print(m,n)
        for i in range(m-1):
            for j in range(n-1):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
                #print(dp[i+1][j+1])

        return dp[m-1][n-1]  