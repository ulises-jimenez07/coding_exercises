def add_without_plus(a,b):
    while b!=0:
        _sum = a^b
        carry=(a & b) << 1
        print (_sum)
        print(carry)
        a=_sum
        b = carry
    return a

print(add_without_plus(   1001, 234))