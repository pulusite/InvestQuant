import TreeNode
class Leet144:
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

leet = Leet144()
root = TreeNode()
treeNode2=TreeNode(2)
treeNode3=TreeNode(3)

print leet.preorderTraversal(leet,root)

