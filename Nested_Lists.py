n = int(input())
grd = [[],[]]
for _ in range(n):
    grd[0].append(input())
    grd[1].append(float(input()))
    
grds = sorted(set(grd[1]))
second_lowest = grds[1]

ans = [x for x , y in zip(grd[0], grd[1]) if y == second_lowest]
ans.sort()

for z in ans:
    print(z)
