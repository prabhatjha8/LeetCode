class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(items)
        m = len(queries)
        sortedItems = sorted(items)
        
        maxBeauty = -float("inf")
        for i in range(n):
            maxBeauty = max(maxBeauty, sortedItems[i][1])
            sortedItems[i][1] = maxBeauty

        sortedQueries = sorted(list(zip(queries, range(m))))

        ans = {}
        i = 0
        j = 0
        lastMax = 0
        while i < n and j < m:
            if sortedItems[i][0] <= sortedQueries[j][0]:
                lastMax = sortedItems[i][1]
                i += 1 
            else:
                ans[sortedQueries[j][0]] = lastMax
                j += 1

        if m - j > 0:
            for k in range(j, m):
                ans[sortedQueries[k][0]] = lastMax

        final_ans = [-1 for _ in range(m)]
        for item in sortedQueries:
            final_ans[item[1]] = ans[item[0]]

        return final_ans
            






        
        

        