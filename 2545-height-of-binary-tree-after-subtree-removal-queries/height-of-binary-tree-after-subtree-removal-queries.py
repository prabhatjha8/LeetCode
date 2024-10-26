# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        # first I will update the level of every node in a dict, level would be key and the value would be a dictionary constaining all nodes with that level

        levelToNodes = defaultdict(lambda: {}) # key is level, value is dict whose key is node_val at that layer and value is height of tree with this node as root
        nodeToDistance = {}
        queue = deque()

        queue.append(root)
        nodeToDistance[root.val] = 0
        levelToNodes[0][root.val] = -1

        while queue:
            node = queue.popleft()

            if node.left:
                nodeToDistance[node.left.val] = nodeToDistance[node.val] + 1
                levelToNodes[nodeToDistance[node.left.val]][node.left.val] = -1
                queue.append(node.left)

            if node.right:
                nodeToDistance[node.right.val] = nodeToDistance[node.val] + 1
                levelToNodes[nodeToDistance[node.right.val]][node.right.val] = -1
                queue.append(node.right)

        # now we find the height of the tree defined by every node

        # first I define isleaf
        def isLeaf(node):
            if not (node.left or node.right):
                return True
            return False

        def helper_fn(node):

            if not node:
                return 0

            elif isLeaf(node):
                levelToNodes[nodeToDistance[node.val]][node.val] = 0
                return 0

            else:
                value = 1 + max(helper_fn(node.left), helper_fn(node.right))
                levelToNodes[nodeToDistance[node.val]][node.val] = value
                return value

        helper_fn(root)

        # Now i have levelToNodes disctionary fully filled, now i can find the ans
        # the algorithm is to sort the values of levelToNodes for every level, on value of the value, for example sort levelToNodes[0] on value of levelToNodes[0]
        levelToNodes = {i: sorted(j.items(), key = lambda x: x[1]) for i, j in levelToNodes.items()}
        levelToItemCount = {i:len(j) for i,j in levelToNodes.items()}

        maxDepth = levelToNodes[0][0][1]

        ans = []
        for query in queries:
            level = nodeToDistance[query]
            allBrothers = levelToNodes[level]
            if allBrothers[-1][0] == query:
                if levelToItemCount[level] == 1:
                    ans.append(level-1)
                else:
                    ans.append(allBrothers[-2][1] + level)
            else:
                ans.append(maxDepth)

        return ans 
                    





