class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
      
    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        """
        # Brute Force
        tmp = []
        minimum_value = self.stack[-1]

        while len(self.stack):
            minimum_value = min(minimum_value, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())

        return minimum_value
        """

        
        
