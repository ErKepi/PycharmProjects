def f(a: object, b: object, c: object, d: object) -> object:
    return (not a and not b and not c and d) or (not a and b and not c and not d) or (not a and b and not c and d) or (
            not a and b and c and d) or (a and not b and c and not d) or (a and not b and c and d) or (
            a and b and not c and d) or (a and b and c and not d) or (a and b and c and d)


print(f(0, 0, 0, 1))
print(f(0, 1, 0, 0))
