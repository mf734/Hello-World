'''
打印从1到最大的n位数
输入数字n,按顺序打印出从1到最大的n位十进制数，
比如输入3，则打印出1、2、3一直到最大的3位数999.

解题思路：需要考虑大数问题，这是题目设置的陷阱。
可以把问题转换成数字排列问题，用递归让代码更简洁。
'''
class Solution:
	def printToMax(self, n):
		if n <= 0:
			return
		number = ['0']*n
		for i in range(10):
			number[0] = str(i)
			self.helper(number, n, 0)
	def prin(self, number):
		is0 = True
		nLen = len(number)
		for i in range(nLen):
			if is0 and number[i] != '0':
				is0 = False
			if not is0:
				print('number[i]')
		print('\t')
	def helper(self, number, length, index):
		if index == length - 1:
			self.prin(number)
		for i in range(10):
			number[index+1] = str(i)
			self.helper(number, length, index+1)