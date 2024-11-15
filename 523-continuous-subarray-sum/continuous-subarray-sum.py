class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        reminderIndies = defaultdict(list)
        reminderIndies[0].append(-1)
        sm = 0
        for i in range(n):
            sm += nums[i]
            val = sm%k
            reminderIndies[val].append(i)
            if reminderIndies[val][-1] - reminderIndies[val][0] > 1:
                return True
        return False
        
        