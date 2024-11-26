class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        InDegree = defaultdict(int)
        for edge in edges:
            InDegree[edge[1]] += 1

        strongestGuy = None
        strongestGuyCount = 0
        for node in range(n):
            if InDegree[node] == 0:
                strongestGuy = node
                strongestGuyCount += 1

                if strongestGuyCount > 1:
                    return -1

        return strongestGuy
            




        