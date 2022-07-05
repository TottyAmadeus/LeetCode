class Solution(object):

    def romanToInt(self, s):
             
        # Roman to Integer Mapping

        romanLettersValue = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # It's easier to solve roman numerals from the end to the beginning
        # So we reverse the string

        s = s[::-1]

        # We will store the sum of the roman numerals to return it later
        sum = 0

        #For each letter in the string we will check if it's a roman numeral
        for letter in s:
            if letter in romanLettersValue:

                # If it is a roman numeral we will add it to the num
                num = romanLettersValue[letter]

                # If 4 times the number is bigger than the sum, it means that it is those specific cases like (IV, IX, XL, XC, CD, CM)
                # So we will subtract the number from the sum

                # Example: IV = 4
                # First Interation: sum = 0, num = 5: sum = 5
                # Second Interation: sum = 5, num = 1: (as 4 * num < sum) sum = 4

                if 4 * num < sum: sum -= num
                else: sum += num

        return sum