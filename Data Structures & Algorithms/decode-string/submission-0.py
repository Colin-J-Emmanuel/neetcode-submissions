class Solution:
    def decodeString(self, s: str) -> str:
        number_stack = [] # stores digit characters from the string
        string_stack = [] # stores the letter characters (and the opening bracket)

        i = 0
        while i < len(s):
            c = s[i]

            # 1: If we get a number, we parse the full multi-digit number and push it onto the number_stack
            if c.isdigit():
                k = 0
                while i < len(s) and s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                number_stack.append(k)
                continue # because we have already advanced i

            # 2: If we get anything other than "]", push it onto string_stack
            if c != "]":
                string_stack.append(c)
                i += 1
                continue

            # 3: If we get a "]", pop the string_stack until "[" to form a chunk, and then repeat it
            chunk = []
            while string_stack and string_stack[-1] != "[":
                chunk.append(string_stack.pop())
            string_stack.pop() # this removes "["

            chunk.reverse()
            chunk_str = "".join(chunk)

            repeat = number_stack.pop()
            expanded = chunk_str * repeat

            # push the expanded string back onto the string_stack (as one token is fine)
            string_stack.append(expanded)

            i += 1

        return "".join(string_stack)

