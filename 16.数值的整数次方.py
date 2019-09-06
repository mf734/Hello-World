class Solution:
	def Power1(self, base, exponent):
		ans = 1
		if exponent > 0:
			for i in range(exponent):
				ans *= base
		elif exponent == 0:
			return 1
		else:
			for i in range(-exponent):
				ans *= base
			ans = 1/ans
		return ans

# 当n为偶数，a^n = a^(n/2) * a^(n/2)
# 当n为奇数，a^n = a^((n-1)/2) * a^((n-1)/2)) * a
# 右移一位运算代替除以2，更快速
class Solution():
	def Power2_fast(self, base, exponent):
		if exponent == 0:
			return 1
		if exponent == 1:
			return base
		if exponent == -1:
			return 1/base
		res = self.Power2_fast(base, exponent>>1)
		res *= res
		if exponent & 0x1 == 1:
			res *= base
		return res
	