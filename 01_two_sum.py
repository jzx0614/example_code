def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	idx_hash = {}
	for idx, num in enumerate(nums):
		if idx_hash.has_key(num):
			return [idx_hash[num], idx]
		else:
			idx_hash[target-num] = idx	

print twoSum([2,7,11,15], 9)