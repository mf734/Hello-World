'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，
请返回0。
'''
class Solution:
	def minN(self, nums):
		if not nums or not isinstance(nums, list):
			return
		lo, mid, hi = 0, 0, len(nums)-1
		# 因为旋转了，所以左边的数字理应比右边的大
		while (nums[lo] >= nums[hi]):
			if (hi - lo) == 1:
				mid = hi
				break
			mid = lo + (hi - lo)//2
			# 以下三句只是为了解决重复的数字
			if nums[hi] == nums[lo] == nums[mid]:
				mid = minV(nums, lo, hi)
				break
			if nums[mid] >= nums[lo]:
				lo = mid
			elif nums[mid] <= nums[hi]:
				hi = mid
		return nums[mid]

	def minV(nums, lo, hi):
		val, midx = nums[lo], lo
		for i in range(lo, hi+1):
			if nums[i] < val:
				val = nums[i]
				midx = i
		return midx