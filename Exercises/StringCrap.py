def f(string, n, c=0):
    if c < n:
        print(string * n)
        f(string, n, c=c + 1)

f('abc', 3)
