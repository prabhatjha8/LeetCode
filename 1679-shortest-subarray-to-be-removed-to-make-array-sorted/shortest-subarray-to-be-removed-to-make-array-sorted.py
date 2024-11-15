class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        def handle_two(i, j):
            curMin = float("inf")
            k = n - 1
            while i >= 0:
                while (k >= j) and (arr[k] >= arr[i]):
                    print("i, k: ", (i, k))
                    k -= 1

                curMin = min(curMin, k - i)
                print("curMin: ", curMin)
                i -= 1
            return min(curMin, j)

        i = 0
        while i < n - 1 and arr[i+1] >= arr[i]:
            i += 1

        j = n - 1
        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1

        
        print(i, j)

        if i >= j:
            return 0

        elif i == -1:
            return n - 1


        return handle_two(i, j)





            
        