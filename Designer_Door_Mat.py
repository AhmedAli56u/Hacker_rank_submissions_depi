# Enter your code here. Read input from STDIN. Print output to STDOUT
n , m = map(int, input().split())
s = '-'
sh = '.|.'

for i in range(n//2,0, - 1):
    print(s*i*3 + sh * ((n//2 - i + 1) * 2 - 1)+ s*i*3)

print(((m - 7)//2)*s + "WELCOME" + ((m - 7)//2)*s)

for i in range(n//2,0, - 1):
    print(s*(n//2-i+1)*3 + sh * (i * 2 - 1) + s*(n//2-i+1)*3)
