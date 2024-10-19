from collections import deque
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n =  len(grid[0])

        def neighbors(i, j):
            ans = set()
            ans.add((max(i-1, 0), j))
            ans.add((min(i+1, m-1), j))
            ans.add((i, max(j-1, 0)))
            ans.add((i, min(j+1, n-1)))
            return ans

        expectedLength = m*n - 1
        startPoint = None
        endPoint = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    expectedLength -= 1
                elif grid[i][j] == 1:
                    startPoint = (i, j)
                elif grid[i][j] == 2:
                    endPoint = (i, j)

        ans = [0]
        def helper_fn(curPoint, distanceCovered, populatedGrid):
            if (curPoint == startPoint) and (distanceCovered == expectedLength):
                ans[0] = ans[0] + 1
            elif distanceCovered == expectedLength:
                pass
            else: 
                for neigh in neighbors(curPoint[0], curPoint[1]):
                    if populatedGrid[neigh[0]][neigh[1]] in [0, 1]:
                        newPopulatedGrid = copy.deepcopy(populatedGrid)
                        newPopulatedGrid[neigh[0]][neigh[1]] = -1
                        helper_fn(neigh, distanceCovered + 1, newPopulatedGrid)
            
        helper_fn(endPoint, 0, grid)

        return ans[0]



        