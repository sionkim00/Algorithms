        else:
            return False

    def getRandom(self) -> int:
            self.set.remove(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.set:

            self.set.add(val)
            return True
        vals = list(self.set)

        i = random.randint(0, len(vals) - 1)
        return vals[i]
[
