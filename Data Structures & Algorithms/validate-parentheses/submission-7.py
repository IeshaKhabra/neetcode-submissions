class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        my_dict = {'(':')', '[':']', '{':'}'}

        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
        
            else:
                if len(stack) > 0:
                    if my_dict[stack.pop()] == char:
                        continue
                    else:
                        return False
                return False
        return len(stack) == 0