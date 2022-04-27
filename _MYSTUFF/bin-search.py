'''

Given a circularly sorted array of distinct integers, find the total number of times the array is rotated. You may assume that the rotation is in anti-clockwise direction.

Input: [8, 9, 10, 2, 5, 6]
Output: 3

Input: [2, 5, 6, 8, 9, 10]
Output: 0

'''
from typing import List


'''
#fails on timeout
class Solution:
	def findRotationCount(self, nums: List[int]) -> int:
		# check easy cases
		if(nums == [] or nums[len(nums)-1] > nums[0]):
			return 0

		# grab middle
		mid = len(nums)//2
		first = 0
		last = len(nums)-1

		# print("{0} {1} {2}".format(first, mid, last))
		# if middle is smaller than the element to the right of it, then its our thing
		while((mid+1 < len(nums)) and (nums[mid] < nums[mid+1])):
			# if middle is smaller than first, shift left
			if(nums[mid] < nums[first]):
				last = mid - 1
			# if middle is bigger than first, shift right
			if(nums[mid] > nums[first]):
				first = mid + 1
			mid = (last+first)//2
			# print("{0} {1} {2}".format(first, mid, last))
		return (mid+1)


sol = Solution();
print("=====")
print(sol.findRotationCount( [2, 5, 6, 8, 9, 10])) # 0
print("=====")
print(sol.findRotationCount( [8, 9, 10, 2, 5, 6])) # 3
print("=====")
print(sol.findRotationCount( [5, 6, 8, 9, 10, 2])) # 1
print("=====")
print(sol.findRotationCount( [])) # 0
print("=====")
print(sol.findRotationCount( [2])) # 0
print("=====")
print(sol.findRotationCount( [9, 2, 3, 5, 7])) # 1
print("=====")
print(sol.findRotationCount( [9, 2, 3, 5, 7])) # 1
print("=====")

'''

#funny python solution
# class Solution:
# 	def findRotationCount(self, nums: List[int]) -> int:
# 		if len(nums) == 1 or nums == [] or nums[0] < nums[len(nums)-1]:
# 			return 0
# 		return nums.index(max(nums)) + 1
