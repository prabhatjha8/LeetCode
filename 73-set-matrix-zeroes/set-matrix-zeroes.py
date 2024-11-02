class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        def update(i, j):
            matrix[i][j] = float("inf")
            for l in range(n):
                if matrix[i][l] != 0:
                    matrix[i][l] = float("inf")

            for k in range(m):
                if matrix[k][j] != 0:
                    matrix[k][j] = float("inf")


        m,  n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    update(i, j)


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0

