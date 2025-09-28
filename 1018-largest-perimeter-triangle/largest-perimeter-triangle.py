class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        # takes in sorted array and finds the largest perimeter triangle with last value included 
        def helper_fn(arr):
            n = len(arr)
            if n < 3:
                return 0
            else:
                ans = 0
                if arr[-3] + arr[-2] > arr[-1]:
                    return arr[-1] + arr[-2] + arr[-3]
                else:
                    return 0

        nums = sorted(nums)
        n = len(nums)
        ans = 0
        j = n - 1

        while j >= 0:
            ans = max(ans, helper_fn(nums[:j+1]))
            j -= 1

        return ans


        