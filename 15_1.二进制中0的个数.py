# 二进制中0的个数
def num(self, n):
	count = 0
	while n != 0:
		if (n & 1) != 1:
			count += 1
		n >>= 1
	return count

# 二进制高位连续0的个数
# 就是第一位1前面的0的个数
# 默认32位
# 0x8000000就是第一位是1，后面所有都是0
def num2(self, n):
	if n == 0:
		return 32
	count = 0
	mask = 0x80000000
	j = n & mask
	# j为1时则高位0数完了
	while j == 0:
		count += 1
		n <<= 1
		j = n & mask
	return count