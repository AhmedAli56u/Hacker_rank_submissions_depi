N = int(input())
lis = []

for _ in range(N):
    s = map(str, input().split())
    s = list(s)
    if s[0] == "append":
        x = int(s[1])
        lis.append(x)
    elif s[0] == "print":
        print(lis)
    elif s[0] == "remove":
        x = int(s[1])
        if x in lis:
            lis.remove(x)
    elif s[0] == "insert":
        x = int(s[1])
        y = int(s[2])
        lis.insert(x, y)
    elif s[0] == "sort":
        lis.sort()
    elif s[0] == "pop":
        lis.pop()
    elif s[0] == "reverse":
        lis.reverse()
