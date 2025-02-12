class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        def digitSum(num):
            numStr = str(num)
            ans = 0
            for digit in numStr:
                ans += int(digit)
            return ans 

        sumDict = defaultdict(list)
        for num in nums:
            sumDict[digitSum(num)].append(num)
        
        ans = -1
        for sNum in sumDict:
            l = sumDict[sNum]
            if len(l) > 1:
                ans = max(ans, l[-1] + l[-2])

        return ans 


        