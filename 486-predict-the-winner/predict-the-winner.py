class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        dp_dict = defaultdict(lambda : -1)

        def helper_fn(i, j):
            if dp_dict[(i, j)] != -1:
                return dp_dict[(i, j)]

            elif i == j:
                return nums[i]
            
            elif j - i == 1:
                return max(nums[i], nums[j])

            else:
                
                val1 = nums[i] + min(helper_fn(i+1, j-1), helper_fn(i+2, j))
                val2 = nums[j] + min(helper_fn(i, j-2), helper_fn(i+1, j-1))
                dp_dict[(i, j)] = max(val1, val2)

                return dp_dict[(i, j)]

        first_optimal_val = helper_fn(0, n-1)

        return (first_optimal_val >= sum(nums) - first_optimal_val)


        