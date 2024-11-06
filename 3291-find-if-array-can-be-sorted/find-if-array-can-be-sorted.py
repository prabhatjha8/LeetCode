class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

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
                newList.append((min(nums[baseIndex:i]), max(nums[baseIndex:i])))
                baseIndex = i

        newList.append((min(nums[baseIndex:i+1]), max(nums[baseIndex:i+1])))

        for i in range(1, len(newList)):
            if newList[i][0] < newList[i-1][1]:
                return False

        return True


        