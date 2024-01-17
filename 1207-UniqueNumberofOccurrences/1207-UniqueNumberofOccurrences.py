
        for e in arr:
            counter[e] += 1
        s = set()
        for key in counter:

            s.add(counter[key])
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)
class Solution:

            if counter[key] in s:
                return False
        return True
[
