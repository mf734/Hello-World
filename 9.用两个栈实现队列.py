# 两个栈实现队列
class Solution:
	def __init__(self):
		# stack1用于push，2用于pop
		self.stack1 = []
		self.stack2 = []
	def push(self, node):
		self.stack1.append(node)
	def pop(self):
		#如果stack2已经有，直接pop
		if self.stack2:
			return self.stack2.pop()
		#如果stack2没有，而且stack1也没有，直接none
		elif not self.stack1:
			return None
		#如果stack2没有，但是1有，则把它们append进2中
		else:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			return self.stack2.pop()

# 两个队列实现栈
class Solution:
	def __init__(self):
		self.queue1 = []
		self.queue2 = []
	def push(self, node):
		self.queue1.insert(0, node)
	def pop(self):
		if not self.queue1:
			return None
		while self.queue1:
			self.queue2.insert(0, self.queue1.pop())
		self.queue1, self.queue2 = self.queue2, self.queue1
		return self.queue2.pop()