# now how do i ensure no duplicates, idea: if two sum do not give duplicates and then i look for unique smallest value,
# like if "first" is the smallest value, and all the tuple for this is unique then no two solutions would be same 



class Solution:
    def threeSum(self, nums):

        def two_sum_general(sm, arr):

            di = defaultdict(int)
            for num in arr:
                di[num] += 1

            n = len(arr)
            if n < 2:
                return []

            unique_nums = sorted(di.keys())
            m = len(unique_nums)
            i = 0
            j = m - 1
            
            ans = []
            while i < j:
                if unique_nums[i] + unique_nums[j] == sm:
                    ans = ans + [[unique_nums[i], unique_nums[j]]]
                    i += 1
                    j -= 1

                elif unique_nums[i] + unique_nums[j] < sm:
                    i += 1

                else: 
                    j -= 1

            if (sm % 2 == 0) and di[sm//2] >=2:
                ans = ans + [[sm//2, sm//2]]

            return ans 

        ans = []
        nums = sorted(nums)
        n = len(nums)
        ans = ans + [[nums[0]] + couple for couple in two_sum_general(-1*nums[0], nums[1:])]

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                first_num = nums[i]
                valid_couple = two_sum_general(-1*first_num, nums[i+1:])
                valid_couple_extended = [[first_num] + couple for couple in valid_couple]
                ans = ans + valid_couple_extended

        return ans

