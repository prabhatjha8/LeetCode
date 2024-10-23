# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        nodeToDepth = {root: 0}
        nodeToParent = {root:-1}
        depthToNodes = defaultdict(list)
        depthToNodes[0].append(root)

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()

            if node.left:
                depth = 1 + nodeToDepth[node]
                nodeToDepth[node.left] = depth
                depthToNodes[depth].append(node.left)
                nodeToParent[node.left] = node
                queue.append(node.left)

            if node.right:
                depth = 1 + nodeToDepth[node]
                nodeToDepth[node.right] = depth
                depthToNodes[depth].append(node.right)
                nodeToParent[node.right] = node
                queue.append(node.right)

        root.val = 0
        totalDepth = max(depthToNodes.keys())
        for dep in range(1, totalDepth+1):
            parentValDict = defaultdict(int)
            totalSum = 0
            for node in depthToNodes[dep]:
                parentValDict[nodeToParent[node]] += node.val
                totalSum += node.val
            for node in depthToNodes[dep]:
                node.val = totalSum - parentValDict[nodeToParent[node]]

        return root

