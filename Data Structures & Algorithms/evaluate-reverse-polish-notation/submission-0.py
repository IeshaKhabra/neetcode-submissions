class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token in ("+", "-", "/", "*"):
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    result = left + right

                elif token == "-":
                    result = left - right
                
                elif token == "/":
                    result = int(left / right)
                
                else:
                    result = left * right
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]