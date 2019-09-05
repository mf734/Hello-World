'''
以下的例子都是对斐波那契的延伸。
'''

# 青蛙跳，矩阵覆盖
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
class jumpSolution():
	# 解法：如果第一次跳一阶，那么剩下n-1个台阶
	# 同理跳两阶就剩n-2。不管剩多少，都可以继续这样拆分问题
	def jump(self, n):
		res = [1, 2]
		while len(res) <= n:
			res.append(res[-1]+res[-2])
		if n == 1:
			return 1
		else:
			return res[n-1]
# 变态跳
# f(n) = f(n-1) + f(n-2) + ... + f(1)
# f(n-1) = f(n-2) + ... + f(1)
class btjump():
	def btjum1(self, n):
		return 2**(n-1)

	# <<是位运算
	# a<<b是指a*(2^b)
	# a>>b是指a/(2^b)
	def btjum2(self, n):
		return 1 << (n-1)