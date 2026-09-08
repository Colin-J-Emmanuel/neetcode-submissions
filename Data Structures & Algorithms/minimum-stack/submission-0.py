class MinStack:

    def __init__(self):
        self.stack = []
        # self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
      
    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        tmp = []
        minimum_value = self.stack[-1]

        while len(self.stack):
            minimum_value = min(minimum_value, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())

        return minimum_value

        
        
