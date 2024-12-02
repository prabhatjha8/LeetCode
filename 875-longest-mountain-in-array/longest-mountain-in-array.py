class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        minimas = []
        for i in range(1, n-1):
            if (arr[i] > arr[i+1]) and (arr[i] > arr[i-1]):
                minimas.append(i)

        curLen = 0
        maxLen = 0

        for mi in minimas:
            leftLength = 0
            rightLength = 0
            j = mi+1
            while (j < n) and (arr[j] < arr[j-1]):
                rightLength += 1
                j += 1

            i = mi - 1
            while (i >= 0) and (arr[i] < arr[i+1]):
                leftLength += 1
                i -= 1

            curLen = leftLength + 1 + rightLength
            maxLen = max(maxLen, curLen)

        if maxLen < 3:
            return 0

        return maxLen




        
        
        
        
        