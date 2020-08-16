class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                import pdb
                pdb.set_trace()
                j = i
                while j < n and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                for k in range((n-i)//2):
                    nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
                break
        else:
            nums.reverse()


if __name__ == "__main__":
    soln = Solution()
    soln.nextPermutation([2,3,1,5,4,2])
                        # 2,3,2,5,4,1
                        # 2 4 3 8 7 6 5 1
                        # 2 4 5 8 7 6 3 1
                        # 2 4 5 1 7 6 3 8
                        # (n-i)//2
                        # a < b > x > y > z > w


                       

