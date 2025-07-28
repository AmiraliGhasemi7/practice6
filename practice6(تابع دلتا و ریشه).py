def delta(a, b, c):
    return b**2 - 4*a*c

def roots(a, b, c):
    d = delta(a, b, c)
    root1 = (-b +(d)) / (2*a)
    root2 = (-b -(d)) / (2*a)
    return root1, root2

# نمونه استفاده:
a = float(input("a=enter your number:"))
b = float(input("b=enter your number:"))
c = float(input("c=enter your number:"))

d = delta(a, b, c)
print(f"دلتا: {d}")

r1, r2 = roots(a, b, c)
print(f"ریشه اول: {r1}")
print(f"ریشه دوم: {r2}")