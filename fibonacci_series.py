x = int(input())
a = 0
b = 1
if x <= 0:
    print(x)
else:
    print(a)
    # print(b)
    for y in range(1,x):
        z = a + b
        a = b
        b = z

        print("fibonacci series like this=",a)