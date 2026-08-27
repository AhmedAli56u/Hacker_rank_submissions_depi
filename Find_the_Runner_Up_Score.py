n = int(input())
arr = map(int, input().split())
arr = list(arr)
arr.sort()

ans = -100

for num in arr:
    if num > ans and num != arr[-1] :
        ans = num
        
print(ans)
