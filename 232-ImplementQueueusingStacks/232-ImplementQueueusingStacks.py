            while self.s1:
                self.s2.append(self.s1.pop())

        return len(self.s2) == 0


    def empty(self) -> bool:
        if not self.s2:
        return self.s2[-1]

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

[
