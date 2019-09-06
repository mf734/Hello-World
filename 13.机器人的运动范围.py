class Solution:
	def movingCount(self, threshold, rows, cols):
		if threshold < 0 or rows <= 0 or cols <= 0:
			return 0
		visited = [None for i in range(rows) for j in range(cols)]
		count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)
		return count

	def movingCountCore(self, threshold, rows, cols, i, j, visited):
		if self.check(threshold, rows, cols, i, j, visited):
			visited[i*cols+j] = True
			value = 1 + self.movingCountCore(threshold, rows, cols, i-1, j, visited) + \
			self.movingCountCore(threshold, rows, cols, i+1, j, visited) + \
			self.movingCountCore(threshold, rows, cols, i, j-1, visited) + \
			self.movingCountCore(threshold, rows, cols, i, j+1, visited)
		return value

	def check(self, threshold, rows, cols, i, j, visited):
		if 0 <= i < rows and 0 <= j < cols and \
		self.getDigitNum(i) + self.getDigitNum(j) <= threshold and \
		not visited[i*cols+j]:
			return True
		return False

	def getDigitNum(self, x):
		res = 0
		while(x>0):
			res += x%10
			x = x//10
		return res