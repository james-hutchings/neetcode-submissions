class MinStack:
    # Core idea is to use two stacks. One main and one minstack.

    def __init__(self):
        self.stack = []

        # In the minstack, each position is the MIN at that point.
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Appends if possible.
        val = min(val, self.minStack[-1] if self.minStack else val)
        self. minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
