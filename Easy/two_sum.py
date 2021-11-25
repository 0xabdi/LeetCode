class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        
        Brute Force Method:
        for i in range(len(nums)):
            for j in range(len(nums)+1):
                num_sum = nums[i] + nums[j]
                if num_sum == target:
                    return [i,j]
        """
        
        nums_dict = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return[i, nums_dict[complement]]
            nums_dict[nums[i]] = i
        
        