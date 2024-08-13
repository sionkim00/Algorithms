    def pop(self) -> int:
        return self.q1.pop()


    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0


[
["MyStack","push","push","top","pop","empty"]
[[],[1],[2],[],[],[]]
[null,null,null,2,2,false]
[null,null,null,2,2,false]
