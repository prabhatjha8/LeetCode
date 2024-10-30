class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        def findIncreasingSubsequence(nums):
            increasingDPDict = defaultdict(lambda : 1)
            increasingDPDict[0] = 1 
            for i in range(1, n):
                maxLen = 1
                for j in range(i):
                    if nums[j] < nums[i]:
                        maxLen = max(maxLen, 1 + increasingDPDict[j])
                increasingDPDict[i] = maxLen
            return increasingDPDict

        def findDecreasingSubsequence(nums):
            decreasingDPDict = defaultdict(lambda : 1)
            decreasingDPDict[n-1] = 1 
            for i in range(n-2, -1, -1):
                maxLen = 1
                for j in range(i+1, n):
                    if nums[j] < nums[i]:
                        maxLen = max(maxLen, 1 + decreasingDPDict[j])
                decreasingDPDict[i] = maxLen
            return decreasingDPDict

        increasingDPDict = findIncreasingSubsequence(nums)
        decreasingDPDict = findDecreasingSubsequence(nums)

        ans = float("inf")
        for i in range(1, n-1):
            dropped_guys = (i + 1 - increasingDPDict[i]) + (n - i - decreasingDPDict[i]) 
            if (increasingDPDict[i] > 1) and (decreasingDPDict[i] > 1):
                ans = min(ans, dropped_guys)

        return ans

        