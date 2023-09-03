class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

        An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

        Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # you can not set up [ [1] * n ] * m, all the rows will point to the first row
        dp = [[1] * n for _ in range(m)]

        # preset the value on the obstacle as obstable to 0
        # preset the value 0 on the right if obstable in the first row
        # preset the value 0 on the bottom if obstacle in the first col
        #print(dp[0])
        k = -1
        # row 0
        for j in range(n):
            #print('row 0 : col{j}')
            if obstacleGrid[0][j]  == 1:
                k = 1
                dp[0][j] = 0
                print('set 0 a')
            elif k == 1:
                dp[0][j] = 0
                print('set 0 b')
        #print(dp)        
        # col 0
        k = -1
        for i in range(1,m):
            if obstacleGrid[i][0]  == 1:
                k = 1
                dp[i][0] = 0
            elif k == 1:
                dp[i][0] = 0
#        print(dp)
        

        for i in range(m-1):
            for j in range(n-1):
                
                if obstacleGrid[i+1][j+1] == 1:
                    dp[i+1][j+1] = 0
                else:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]

        return dp[m-1][n-1]
        