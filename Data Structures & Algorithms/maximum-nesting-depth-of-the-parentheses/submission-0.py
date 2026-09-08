class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0 # keeps track of the number of parentheses
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
                result = max (result, len(stack))
            elif c == ")":
                stack.pop()

        return result
        