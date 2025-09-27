class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        def num_long_distance_couple(dis, arr):
            # arr is sorted
            # returns a dict with keys arr[i] + dis for all i,
            # the value is len([j for j in arr if j > arr[i] + dis)
            n = len(arr)
            baseline = [arr[alpha] + dis for alpha in range(n)]
            ans = defaultdict(int)
            count = 0

            # arr[i] + dis > arr[j]

            i = 0
            j = 0
            while i < n and j < n:
                if arr[j] < arr[i] + dis:
                    count += 1
                    j += 1
                else:
                    ans[i] = (count - i - 1)
                    i += 1

            while i < n:
                ans[i] = (count - i - 1)
                i += 1

            return sum(ans.values())

        nums = sorted(nums)

        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1

        nums = nums[i:]
        
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            ans += num_long_distance_couple(nums[i], nums[i+1:])

        return ans

                

                

    






        