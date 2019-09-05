'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如: 
'a b c e 
 s f c s 
 a d e e' 
矩阵中包含一条字符串”bcced”的路径，但是矩阵中不包含”abcb”路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。
'''

# 用回溯法加递归
class Solution:
	def hasPath(nums, s1):
		if not nums or not s1:
			return
		# 建二维矩阵
		rows, cols = len(nums), len(nums[0])
		for i in range(rows):
			for j in range(cols):
				if nums[i][j] = s1[0]:
					if hasPathCore(nums, s1[1:], rows, cols, i, j):
						return True
		return False

	def hasPathCore(nums, s1, rows, cols, i, j):
		if not s1:
			return True
		if j + 1 < cols and s1[0] == nums[i][j+1]:
			return hasPathCore(nums, s1[1:], rows, cols, i, j+1)
		elif j - 1 >= 0 and s1[0] == nums[i][j-1]:
			return hasPathCore(nums, s1[1:], rows, cols, i, j-1)
		elif i + 1 < rows and s1[0] == nums[i+1][j]:
			return hasPathCore(nums, s1[1:], rows, cols, i+1, j)
		elif i - 1 >= 0 and s1[0] == nums[i-1][j]:
			return hasPathCore(nums, s1[1:], rows, cols, i-1, j)
		else:
			return False

class Solution:
	def hasPath(self, matrix, rows, cols, path):
		if not matrix or rows<0 or cols<0 or path==None:
			return False
		visited = [False]*(len(matrix))
		pathIndex = 0
		for i in range(rows):
			for j in range(cols):
				if self.hasPathCore(matrix, rows, cols, i, j, path, pathIndex, visited):
					return True
		return False

	def hasPathCore(self, matrix, rows, cols, x, y, path, pathIndex, visited):
		'''
		x, y 当前对应的横纵坐标
		path 目标路径
		visited 是否访问过
		pathIndex 已经找到的路径长度
		'''
		if pathIndex == len(path):
			return True
		curPath = False
		# 位置坐标不超过行列数
		# 当前坐标和目标路径对应字符一样
		# 没有被走过
		if 0 <= x < cols and 0 <= y < rows \
			and matrix[y*cols + x] == path[pathIndex] \
			and not visited[y*cols + x]:
			visited[y*cols + x] = True
			pathIndex += 1
			curPath = self.hasPathCore(matrix, rows, cols, x-1, y, path, pathIndex, visited) \
			or self.hasPathCore(matrix, rows, cols, x, y-1, path, pathIndex, visited) \
			or self.hasPathCore(matrix, rows, cols, x+1, y, path, pathIndex, visited) \
			or self.hasPathCore(matrix, rows, cols, x, y+1, path, pathIndex, visited)
			if not curPath:
				pathIndex -= 1
				visited[y*cols + x] = False
		return curPath