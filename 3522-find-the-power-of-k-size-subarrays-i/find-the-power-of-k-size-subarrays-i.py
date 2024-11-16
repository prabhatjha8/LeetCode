class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        def findActuteSlope(arr):
            n = len(arr)
            i = n - 1
            while (i > 0) and (arr[i-1] == arr[i] - 1):
                i -= 1
            return i

        sweetPoint = findActuteSlope(nums[:k])
        print("sweetPoint: ", sweetPoint)

        ans = []
        n = len(nums)
        
        i = 0
        j = k - 1

        while j < n - 1:
            if i == sweetPoint:
                ans.append(nums[j])

                if nums[j+1] != nums[j] + 1:
                    sweetPoint = j + 1

                else:
                    sweetPoint += 1

            else:
                ans.append(-1)
                if nums[j+1] != nums[j] + 1:
                    sweetPoint = j + 1

     
            i += 1
            j += 1

        if i == sweetPoint:
            ans.append(nums[-1])
        
        else:
            ans.append(-1)

        return ans

        




        