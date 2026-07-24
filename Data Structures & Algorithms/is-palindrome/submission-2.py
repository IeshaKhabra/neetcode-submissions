class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """
        two pointer

        left at beginning
        right at end

        check if left and right sides are equal
        if they are then continue
        if not return false
        """

        left = 0
        right = len(s) - 1

        

        while left < right:
            while left < right and s[left].isalnum() == False:
                left += 1
            while left < right and s[right].isalnum() == False:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True