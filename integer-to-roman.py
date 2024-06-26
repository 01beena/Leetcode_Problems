class Solution:
    def intToRoman(self, num: int) -> str:
        def int_to_roman(num):
            roman = ''
            roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
            
            for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
                roman += roman_dict[i] * (num // i)
                num = num % i
                if num == 0:
                    break
            
            return roman
        
        # Call the function and return the result
        return int_to_roman(num)
