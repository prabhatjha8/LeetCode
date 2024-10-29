class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        def neighbours(point):
            i, j = point
            ans = set()
            ans.add((max(i-1, 0), min(j+1, n-1)))
            ans.add((i, min(j+1, n-1)))
            ans.add((min(i+1, m-1), min(j+1, n-1)))
            return ans
        
        m, n = len(grid), len(grid[0])

        dp_col_prev = [1 for _ in range(m)]
        dp_col_cur = [-1 for _ in range(m)]

        for j in range(n-2, -1, -1):
            for i in range(m):
                val = 1
                for point in neighbours((i, j)):
                    if grid[point[0]][point[1]] > grid[i][j]:
                        val = max(val, 1 + dp_col_prev[point[0]])
                dp_col_cur[i] = val
            dp_col_prev = dp_col_cur
            dp_col_cur = [-1 for _ in range(m)]

        return max(dp_col_prev) - 1

                
                        




        