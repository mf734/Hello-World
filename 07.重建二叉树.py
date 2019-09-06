class Solution:
	# 前序、中序
	def reCons(self, pre, tin):
		if not pre or not tin:
			return None
		# 前序的第一个数必定是根节点
		root = TreeNode(pre[0])
		# 根节点在中序中，其左、右部分分别为左、右子树中序遍历结果
		val = tin.index(pre[0])
		# 将其左右部分分别放入。
		# tin中，左边的均为左子树，右边的均为右子树。
		# 所以利用index找到val，即tin中根的index
		# 把tin的val左右的传进去
		# 同时按照个数，把pre的左右也传进去
		# 其中，pre中的[0]已经放入了，所以从1开始
		if len(pre) > 1:
			root.left = self.reCons(pre[1:val+1], tin[:val])
			root.right = self.reCons(pre[val+1:], tin[val+1:])
		return root
