class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        ans = 0
        j = n - 1
        while j >= 2:
            two_sides_sum = nums[j-1] + nums[j-2]
            if two_sides_sum > nums[j]:
                ans = max(ans, two_sides_sum + nums[j])
            j -= 1

        return ans
        