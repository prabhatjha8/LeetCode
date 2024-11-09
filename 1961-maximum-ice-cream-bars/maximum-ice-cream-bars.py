class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        def CountingSort(nums):
            m = min(nums)
            M = max(nums)
            counter = Counter(nums)
            ans = []
            for i in range(m, M+1):
                ans.extend([i] * counter[i])
            return ans

        sortedCosts = CountingSort(costs)

        i = 0
        sm = 0
        while i < n:
            sm += sortedCosts[i]
            if sm > coins:
                return i
            i += 1

        return n

        




        