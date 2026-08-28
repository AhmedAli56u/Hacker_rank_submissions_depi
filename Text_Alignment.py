n = int(input())
c = 'H'

for i in range(n):
    print((c * (i * 2 + 1)).center(n * 2))

for _ in range(n + 1):
    print((c * n).center(n * 2) + (c*n).center(n * 6))

for _ in range((n + 1)//2):
    print((c * n * 5).center(n * 6))

for _ in range(n + 1):
    print((c * n).center(n * 2) + (c*n).center(n * 6))

for i in range(n*2 - 1 , 0, -2):
    print((c * (i)).center(n * 10))
