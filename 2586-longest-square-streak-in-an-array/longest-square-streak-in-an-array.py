class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        existenceDict = defaultdict(int)
        for num in nums:
            existenceDict[num] = 1

        nums = sorted(nums)

        dp_dict = defaultdict(int)
        dp_dict[nums[-1]] = 1

        n = len(nums)

        for i in range(n-2, -1, -1):
            dp_dict[nums[i]] = dp_dict[nums[i]**2] + 1

        ans = max(dp_dict.values())
        if ans == 1:
            return -1
        else:
            return ans





        
        
        