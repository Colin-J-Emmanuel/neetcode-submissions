class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {'(':')', '{':'}', '[':']'}

        for character in s:
            if character in matching_brackets: # if the character is an opening bracket
                stack.append(character)
            elif character in matching_brackets.values(): # if the character is a closing bracket
                if not stack or matching_brackets[stack.pop()] != character:
                    return False

        return not stack
