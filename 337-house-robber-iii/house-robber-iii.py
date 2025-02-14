# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def isLeaf(node):
            if (node != None) and (node.left == None) and (node.right == None):
                return True 
            return False 

        dp_dict = defaultdict(lambda : -1)

        def helper_fn(node):
            if dp_dict[node] != -1:
                return dp_dict[node]

            elif node == None:
                return 0

            elif isLeaf(node):
                return node.val

            else:
                valid_nodes = []
                if node.left != None:
                    valid_nodes.append(node.left.left)
                    valid_nodes.append(node.left.right)
                if node.right != None:
                    valid_nodes.append(node.right.left)
                    valid_nodes.append(node.right.right)

                valid_node_vals = 0
                for vn in valid_nodes:
                    valid_node_vals += helper_fn(vn)

                dp_dict[node] = max(node.val + valid_node_vals, helper_fn(node.left) + helper_fn(node.right))

                return dp_dict[node]


        return helper_fn(root)

        
        