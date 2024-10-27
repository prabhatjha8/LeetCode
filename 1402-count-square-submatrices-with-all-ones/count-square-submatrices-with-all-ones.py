from collections import defaultdict
from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        valid_start = defaultdict(int)
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    valid_start[(i, j)] = 1
                    ans += 1
        

        for size in range(2, min(m, n) + 1):
            new_start = defaultdict(int)
            
            for start in list(valid_start.keys()):
                i, j = start
                if (i + size - 1 < m) and (j + size - 1 < n) and \
                   (matrix[i + size - 1][j] == 1) and (matrix[i][j + size - 1] == 1) and \
                   (valid_start[(i + 1, j + 1)] == 1):
                    new_start[(i, j)] = 1
                    ans += 1
            
            valid_start = new_start  

        return ans
