class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        """

        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i
            
        
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums_dict and i != nums_dict[temp]:
                return sorted([i, nums_dict[temp]])
                