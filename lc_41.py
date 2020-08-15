class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            while(1 <= nums[i] <= len(nums) and nums[i]-1 != i):
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        
        for i in range(0, len(nums)):
            if nums[i]-1 != i:
                return i+1
        
        return len(nums)+1




if __name__ == '__main__':
    final_soln = Solution()
    final_soln.firstMissingPositive([3,4,-1,1])

# nums[i] = nums[nums[i]-1]

# i = 2
# [1,7,3,4]
# correctPos = nums[2]-1
# nums[1] == nums[3]
# 7 4 3 1
# 7 1 3 4
# 1 7 3 4


# [1, 1]
# nums[1] != nums[0]
# nums[1] == nums[0]

# 3 .. 2
# 3 - 1 = 2
# nums[i] != nums[2]