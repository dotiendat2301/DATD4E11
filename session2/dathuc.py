a = int(input("Nhập a"))
b = int(input("Nhập b"))
c = int(input("Nhập c"))
delta  = b**2 - 4*a*c
print(delta)
if delta > 0:
    print("có nghiệm")
    print("x1 = ", ((-b-delta**1/2))/(2*a))
    print("x2 = ", ((-b+delta**1/2))/(2*a))
elif delta == 0 :
    print("x =", -b/2*a)
else:
    print("Vô Nghiệm")