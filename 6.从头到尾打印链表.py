class Solution:
	# 直接[::-1]
	def printLis(self, listNode):
		if not listNode:
			return []
		ret = []
		head = listNode
		while head:
			ret.append(head.val)
			head = head.next
		return ret[::-1]
	
	# stack
	def print_iter(self, listNode):
		if not listNode:
			return 
		ret = []
		p = head
		while p!= None:
			ret.append(p.data)
			p = p.next
		for i in range(len(ret)):
			print(stack.pop(), end=" ")
	
	# 头插法
	def print2(self, ListNode):
		if not listNode:
			return []
		ret = []
		head = ListNode
		while head:
			ret.insert(0, head.val)
			head = head.next
		return ret

	# recursion
	def print_recu(head):
		if head.next == None:
			return
		p = head
		if p.next != None:
			print_recu(p.next)
		print(p.data, end=" ")