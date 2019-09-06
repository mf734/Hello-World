'''
给定一颗二叉搜索树，请找出其中的第k大的结点。
例如， 
   5 
 3 	 7 
2 4 6 8 
按结点数值大小顺序第三个结点的值为4。
'''
# 二叉搜索树的中序遍历就是一个递增的序列
class Solution:
	def kthNode(self, root, k):
		if k <= 0:	
			return None
		res = []
		self.inOrder(root, res)
		if len(res) < k:
			return None
		return res[k-1]
	def inOrder(self, root, res):
		if not root:
			return None
		if root.left:
			self.inOrder(root.left, res)
		res.append(root)
		if root.right:
			self.inOrder(root.right, res)