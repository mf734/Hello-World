'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

'''
1, 如果node有右子树，则next就是右子树的最左节点
如果node无右子树，那么：
	2, 如果该结点是父的左子结点，那么next就是父结点
	3, 如果该结点是父的右子结点，那么向上遍历，找一个是它父结点的左子结点的结点。
'''

class Solution:
	def GetNext(self, pNode):
		if not pNode:
			return None
		# 如果有右子树，那下一个就是右子树的最左结点（遍历到叶子）
		elif pNode.right:
			tmp = pNode.right
			while tmp.left:
				tmp = tmp.left
			return tmp

		# 没通过上个elif，说明没有右子树
		# 中序，如果next不是右子树，那next就是父
		# 有父结点，而且它还是父结点的右子结点
		# 说明next就是父结点
		elif pNode.next and pNode.next.right == pNode:
			# 一直找有左子结点的父结点
			while pNode.next and pNode.next.left:
				pNode = pNode.next
			return pNode.next
		# 如果是父子结点的左子结点，直接返回父结点
		else:
			return pNode.next