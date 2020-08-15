
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        distinct_num_arr = []
        self.remove_repeating_elements(nums, distinct_num_arr)
        self.quick_select(distinct_num_arr, len(distinct_num_arr)-k, 0, len(distinct_num_arr)-1)

    def remove_repeating_elements(nums, arr):
    	freq_dict = collections.Counter()
    	for idx, number in enumerate(nums):
    		if freq_dict[number] == 0:
    			freq_dict[number] += 1
    			distinct_num_arr.append(number)

    def partition(self, nums, l, r, pivot_idx):
		nums[pivot_idx], nums[l] = nums[l], nums[pivot_idx]
		i = l+1
		j = l+1

		# j is holding the leftmost index > pivot

		# 4 5 6 2 1 . . . . .

		# 4 3 2 6 1 . . . . .

		while (i <= r):
			if nums[i] < nums[0]:
				nums[i], nums[j] = nums[j], nums[i]
				j += 1
			i += 1
		nums[0], nums[j-1] = nums[j-1], nums[0]
		return j-1 # return pivot
    
    def quick_select(self, nums, k, l, r):
        if l == r:
            return nums[k]
        random_pivot_idx = random.randint(l,r)
        swapped_idx = self.partition(nums, l,r, random_pivot_idx)
        if swapped_idx == k:
            return nums[k]
        elif swapped_idx > k:
            return self.quick_select(nums, k, l, swapped_idx-1)
        else:
            return self.quick_select(nums, k, swapped_idx+1, r)


