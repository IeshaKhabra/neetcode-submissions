class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if num - 1 not in numbers:
                # start sequence from the current number
                current_num = num
                current_len = 1

                while current_num + 1 in numbers:
                    current_num += 1
                    current_len += 1
                longest = max(longest, current_len)
        return longest
    
