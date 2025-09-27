class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        n = len(triangle)
        dp_arr = [[-1]*i for i in range(1, n+1)]
        dp_arr[-1] = triangle[-1]

        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                dp_arr[i][j] = triangle[i][j] + min(dp_arr[i+1][j], dp_arr[i+1][j+1])

        return dp_arr[0][0]

        