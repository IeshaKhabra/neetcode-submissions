class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []

        for current_index in range(len(temperatures)):
            while stack and (temperatures[current_index] > temperatures[stack[-1]]):
                previous_index = stack.pop()
                # the number of days you have waited is the difference of both of them
                result[previous_index] = current_index - previous_index
            stack.append(current_index) # this day is waiting for the next warmer tempterature

        return result