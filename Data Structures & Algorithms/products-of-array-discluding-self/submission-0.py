class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left_product = 1
        for i in range(len(nums)):
            # at every index 0, since we have no elements on left so result[0] = 1
            result[i] = left_product
            # include the current number in the left product for the next index
            left_product *= nums[i]
        
        right_product = 1
        for i in range(len(nums) -1, -1 , -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

