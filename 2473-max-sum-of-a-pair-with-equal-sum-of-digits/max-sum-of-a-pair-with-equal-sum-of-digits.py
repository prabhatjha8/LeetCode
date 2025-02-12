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

        def topTwoSum(arr):
            n = len(arr)
            if n <= 1:
                return -1
            else:
                M = max(arr[1], arr[0])
                m = min(arr[1], arr[0])
                for i in range(2, n):
                    if arr[i] >= M:
                        m = M
                        M = arr[i]

                    elif arr[i] > m:
                        m = arr[i]

                return m + M


        
        ans = -1
        for sNum in sumDict:
            l = sumDict[sNum]
            ans = max(ans, topTwoSum(l))

        return ans 


        