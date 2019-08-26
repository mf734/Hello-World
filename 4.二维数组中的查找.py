# 方法一：循环迭代查找
class Solution:
	def Find1(self, target, array):
		if not array:
			return
		row = len(array)
		col = len(array[0])
		for i in range(row):
			for j in range(col):
				if target == array[i][j]:
					return True
		return False

# 二层遍历，从右上角
class Solution:
	def Find(self, target, array):
		if not isinstance(array, list) or len(array) == 0:
			return False
		i, j = 0, len(array[0])-1
		while i < len(array) and j >= 0:
			if array[i][j] < target:
				i += 1
			elif array[i][j] > target:
				j -= 1
			else:
				return True
		return False