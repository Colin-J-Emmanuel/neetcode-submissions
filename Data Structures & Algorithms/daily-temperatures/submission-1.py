class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []

        for i in range(n):
            days = 0 # assumes there's no warmer day

            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    days = j - i
                    break

            result.append(days)

        return result
