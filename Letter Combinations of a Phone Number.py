from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv", 
            "9": "wxyz"
        }

        if len(digits) == 1:
            return [elem for elem in digit_map[digits]]
        else:
            tmp_list = []
            for d in digits:
                if d in digit_map.keys():
                    tmp_list.append(digit_map[d])


from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv", 
            "9": "wxyz"
        }

        if not digits:
            return []

        return [''.join(p) for p in product(*(digit_map[d] for d in digits))]
