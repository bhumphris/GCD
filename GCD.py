def GCD(a,b):
    if b == 0:
        return a
    print GCD(b, a % b)
print GCD(80, 100)
print GCD(20, 40)

