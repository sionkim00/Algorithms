class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        N = len(digits)
        if digits == "":
            return []
        charMap = {
            "2": ["a", "b", "c"],
            "3": ["d","e","f"],
"23"
