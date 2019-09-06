'''二叉树的深度'''
class Solution:
	def treeD(self, root):
		if not root:
			return 0
		left = self.treeD(root.left)
		right = self.treeD(root.right)
		return max(left+right) + 1

'''平衡二叉树'''
class Solution2:
	def treeD(self, root):
		if not root:
			return 0
		left = self.treeD(root.left)
		right = self.treeD(root.right)
		return max(left+right) + 1

	def treeBal(self, root):
		if not root:
			return True
		left = self.treeBal(root.left)
		right = self.treeBal(root.right)
		dif = left - right
		if diff < -1 or diff > 1:
			return False
		return self.treeBal(root.left) and self.treeBal(root.right)