class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i in range(len(nums)):
            if target - nums[i] not in result:
                result[nums[i]] = i
            else:
                return [result[target - nums[i]], i]
        return [-1, -1]
