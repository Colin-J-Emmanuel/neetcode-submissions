class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores a pair of values [temp, index]

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = (idx - stackIdx)
            stack.append((temp, idx))

        return res
      
        # Brute force
        # n = len(temperatures)
        # result = []

        # for i in range(n):
        #     days = 0 # assumes there's no warmer day

        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             days = j - i
        #             break

        #     result.append(days)

        # return result
