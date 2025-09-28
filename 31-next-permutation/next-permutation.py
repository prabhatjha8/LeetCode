class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n - 2

        while (i >= 0) and (nums[i] >= nums[i+1]):
            i -= 1

        if i == -1:
            nums[:] = nums[::-1]

        else:
            j = i+1
            while j < n and nums[j] > nums[i]:
                j += 1

            if j == n:
                nums[i], nums[j-1] = nums[j-1], nums[i]
                nums[i+1:] = nums[i+1:][::-1]

            else:
                j = j - 1
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = nums[i+1:][::-1]
                