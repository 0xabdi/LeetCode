class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        [1,3,5,6]
        7
        
        BruteForce Method O(n)
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif nums[i] > target:
                return i
            elif target > nums[i]:
                if i == len(nums)-1:
                    return i+1
        """
        # Binary Search O(log n)
        l,r = 0,len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid] :
                r = mid - 1
            else:
                l = mid + 1
        return l
        
            