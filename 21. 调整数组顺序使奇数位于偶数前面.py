class solution:
	def dupicate(self, array):
		res1 = []
		res2 = []
		for i in array:
			if i % 2 == 0:
				res1.append(i)
			else:
				res2.append(i)
		return res2 + res1
		