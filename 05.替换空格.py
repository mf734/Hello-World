class Solution:
	# RE, 但是不推荐用
	def replaceSpace(self, s):
		import re
		return re.sub(" ", "%20", s)

	# replace
	def replaceSpace2(self, s):
		return s.replace(" ", "%20")

	'''
	offer解法：
	先计算源字符串数组长度，并统计空格数量
	新字符串数组长度=源数组长度+2*空格数量
	在新字符串数组上，从后向前遍历，通过两个index移动并复制。
	'''
	def replaceSpace3(self, s):
		s = list(s)
		count = 0
		for e in s:
			if e == " ":
				count += 1
		
		# p1为原始字符串数组的index
		p1 = len(s) - 1
		
		s += [None]*(count*2)
		
		# p2为新字符串数组末尾的index
		p2 = len(s) - 1
		while p1 >= 0:
			if s[p1]==' ':
				s[p2] = '0'
				s[p2-1] = '2'
				s[p2-2] = '%'
				p2 -= 3
			else:
				s[p2] = s[p1]
				p2 -= 1
			p1 -= 1
		return ''.join(map(str, s))
