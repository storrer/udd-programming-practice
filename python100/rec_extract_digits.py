def digits(n):
    greater_than_one = True
    count = 0
    while greater_than_one:
        n = n / 10
        greater_than_one = (1 <= n)
        count += 1
    print(count)
    return count
#digits(10)


def rec_dig(n, d=0):
    if n < 1:
        return d
    else:
        n = n/10
        d += 1
        return rec_dig(n,d)
print(rec_dig(10))