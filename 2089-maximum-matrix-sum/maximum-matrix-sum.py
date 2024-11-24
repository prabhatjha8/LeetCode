class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        allSum = 0
        minVal = float("inf")
        for i in range(m):
            for j in range(n):
                allSum += abs(matrix[i][j])
                minVal = min(minVal, abs(matrix[i][j]))

        numNegatives = []
        for i in range(m):
            count = 0
            for j in range(n):
                if matrix[i][j] < 0:
                    count += 1
            numNegatives.append(count%2)

        if sum(numNegatives) % 2 == 0:
            return allSum

        else: 
            return allSum - 2*minVal
        


        