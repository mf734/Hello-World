class Solution:
	def Num0(self, n):
		if n < 0:
			n = n & 0xffffffff
		count = 0
		# 如果当前位是1，count+=1，然后移位
		while n>0:
			if (n & 1) == 1:
				count += 1
			n >>= 1
		return count


	def Num1(self, n):
		# 负数处理
		if n < 0:
			n = n & 0xffffffff
		count = 0
		# and 运算，不断清楚最右边的1
		# 能做多少次就说明有几个1
		while (n):
			# 该位运算去除 n 的位级表示中最低的那一位。
			n = (n-1) & n
			count += 1
		return count


	# 不推荐用，太依赖python
	def Num2(self, n):
		return bin(n&0xffffffff).count('1')