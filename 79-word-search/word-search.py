class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        def neighbors(point):
            i, j = point
            ans = []
            ans.append((max(i-1, 0), j))
            ans.append((i, max(j-1, 0)))
            ans.append((min(i + 1, m-1), j))
            ans.append((i, min(j + 1, n-1)))
            return ans

        def DFS(source):
            visited = [[-1 for _ in range(n)] for _ in range(m)]

            def dfs(source, word, visited):
                # print("source: ", source)
                # print("word: ", word)
                # print("visited: ", visited)

                i, j = source 

                if word == "":
                    return True 
                
                elif len(word) == 1:
                    return (board[i][j] == word)

                else:
                    visited[i][j] = 1
                    # print(f"neighbors({source}): ", neighbors(source))
                    for neigh in neighbors(source):
                        r, s = neigh
                        if (visited[r][s] == -1) and (board[r][s] == word[1]):
                            val = dfs(neigh, word[1:], visited)
                            if val == True:
                                return val
                            visited[r][s] = -1

                    return False

            return dfs(source, word, visited)


        sources = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    sources.append((i, j))

        i = 0
        while i < len(sources):
            if DFS(sources[i]) == True:
                return True
            else:
                 i += 1

        return False

