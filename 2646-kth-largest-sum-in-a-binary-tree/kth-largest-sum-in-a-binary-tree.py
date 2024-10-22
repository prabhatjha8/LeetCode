# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        distanceToSum = defaultdict(int)
        distanceToSum[0] += root.val
        nodeToDistance = {root : 0}
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                nodeToDistance[node.left] = nodeToDistance[node] + 1
                distanceToSum[nodeToDistance[node.left]] += node.left.val
            if node.right:
                queue.append(node.right)
                nodeToDistance[node.right] = nodeToDistance[node] + 1
                distanceToSum[nodeToDistance[node.right]] += node.right.val

        ls = sorted(list(distanceToSum.values()))

        if len(ls) < k:
            return -1
        else:
            return ls[::-1][k-1]
                
                


        