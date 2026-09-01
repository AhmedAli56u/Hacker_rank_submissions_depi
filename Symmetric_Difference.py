# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
st1 = set(map(int,input().split()))
N = int(input())
st2 = set(map(int, input().split()))

lis = list(st1^st2)
lis.sort()

for n in lis:
    print(n)

