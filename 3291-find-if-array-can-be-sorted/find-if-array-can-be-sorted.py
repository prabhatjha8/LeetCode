class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        def getBitCount(num):
            s = bin(num)[2:]
            return Counter(s)["1"]

        bitsCountList = [getBitCount(num) for num in nums]
        newList = []

        i = 1
        baseIndex = 0
        for i in range(1, n):
            if bitsCountList[i] != bitsCountList[i-1]:
                newList = newList + sorted(nums[baseIndex:i])
                baseIndex = i

        newList = newList + sorted(nums[baseIndex:i+1])

        for i in range(n-1):
            if newList[i] > newList[i+1]:
                return False

        return True


                

        
        