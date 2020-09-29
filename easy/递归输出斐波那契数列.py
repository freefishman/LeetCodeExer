def fun(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fun(n-1)+fun(n-2)

print(fun(10))
