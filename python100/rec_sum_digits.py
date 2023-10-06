"""Input Number of digits Cross sum
1234        4               1 + 2 + 3 + 4 = 10
1234567     7               1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
"""

def rec_sum_digits(n, s=0):
    """Extract sum of the digits of an integer"""
    if n < 1:
        return s
    else:
        remainder = n // 10
        digit_value = n % 10
        return rec_sum_digits(remainder, s + digit_value)
    
print(rec_sum_digits(999))