class Solution:
    def punishmentNumber(self, n: int) -> int:

        def allPartitionSum(numStr):
            if numStr == "":
                return [0]
            else:
                m = len(numStr)
                ans = []
                for i in range(1, m+1):
                    val = int(numStr[:i])
                    ans = ans + [val + i for i in allPartitionSum(numStr[i:])]
                return ans 

        ans = 0
        for i in range(1, n+1):
            sqrVal = i**2
            if i in allPartitionSum(str(sqrVal)):
                ans += sqrVal

        return ans 


        