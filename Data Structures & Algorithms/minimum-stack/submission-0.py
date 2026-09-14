class MinStack:

    def __init__(self):
        self.stack = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_arr or val < self.min_arr[-1]:
            self.min_arr.append(val)
        else:
            self.min_arr.append(self.min_arr[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_arr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
