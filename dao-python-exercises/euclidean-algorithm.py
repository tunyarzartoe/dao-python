# def calc_gcd(a, b):
#     if b == 0:
#         return a
    
#     return calc_gcd(b, a%b)

# a = 30
# b = 12
# gcd = calc_gcd(a, b)
# print(f"{a} と {b} の最大公約数は {gcd}")
def calc_gcd(a, b):
    if b == 0:
        return a
    
    return calc_gcd(b, a%b)


def calc_multi_gcd(a):
    n = len(a)
    gcd = a[0]
    for i in range(1, n):
        gcd = calc_gcd(gcd, a[i])

    return gcd


a = [12, 30, 42]
gcd = calc_multi_gcd(a)

for x in a:
    print(x, end=" ")

print(f"の最大公約数は {gcd}")