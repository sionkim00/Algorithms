
        self.minStack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.arr = []

    def __init__(self):
class MinStack:
[
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
[null,null,null,null,-3,null,0,-2]
[null,null,null,null,-3,null,0,-2]
