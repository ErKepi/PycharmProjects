def f(a, b, c):
    return(not a and not b and c) or (not a and b and c) or (a and b and not c) or (a and b and c)

print(f(0, 0, 1))
print(f(0, 1, 1))
print(f(1, 1, 0))
print(f(1, 1, 1))
