def cross_product(n:int):
    digits = len(str(n))
    print(digits)
    product = 1
    for i in range(digits):
        pass
print(cross_product(12))

def multiply_all_digits(value):
    remainder = value // 10
    digit_value = value % 10
    print("multiply_all_digits: %-10d | remainder: %d, digit: %d" %(value, remainder, digit_value))
    if remainder > 0:
        result = multiply_all_digits(remainder)
        print("-> %d * %d = %d" % (digit_value, result, digit_value * result))
        return digit_value * result
    else:
        print("-> " + str(value))
        return value
multiply_all_digits(12)