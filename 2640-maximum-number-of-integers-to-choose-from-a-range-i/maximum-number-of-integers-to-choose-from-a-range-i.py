class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        counter = Counter(banned)
        ans = 0
        curSum = 0
        for i in range(1, n+1):
            if counter[i] == 0:
                curSum += i
                if curSum > maxSum:
                    return ans 
                else:
                    ans += 1
                    
        return ans 

        