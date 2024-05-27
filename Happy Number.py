class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_sum_of_squares(num):
            result = 0
            while num > 0:
                digit = num % 10
                result += digit * digit
                num //= 10
            return result

        seen_numbers = set()

        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = calculate_sum_of_squares(n)

        return n == 1
