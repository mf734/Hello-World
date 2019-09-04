# fibonacci function 

# 普通递归法
def fibo(n):
	if n < 2:
		return 1
	return fibo(n-1) + fibo(n-2)

# 动态规划
def dp_fibo(n):
	table = [0 for i in range(n+1)]
	if n <= 1:
		return 1
	else:
		if table[n-1] == 0:
			table[n-1] = dp_fibo(n-1)
		if table[n-2] == 0:
			table[n-2] = dp_fibo(n-2)
		table[n] = table[n-2] + table[n-1]
	return table[n]

'''
# 自上向下的动态规划
def dp_fibo(n):
	result = output[n]
	if result == None:
		if n == 0:
			result = 0
		elif n == 1:
			result = 1
		else:
			result = dp_fibo(n-1) + dp_fibo(n-2)
			output[n] = result
	return result
'''
'''
def dp2_fibo(n):
	output = [0]*n
	for i in range(1, n):
		for j in range(0, i):
			output[i] += output[j]
		return output[n-1]
'''

# 自下向上的递推
def bu_fibo(n):
	if n < 2:
		return 1
	t1 = 0
	t2 = 1
	for i in range(2, n+1):
		t1, t2 = t2, t1 + t2
	return t1

# 生成器
def fib_loop(n):
	a, b = 0, 1
	while n > 0:
		a, b = b, a + b
		max -= 1
		yield a
