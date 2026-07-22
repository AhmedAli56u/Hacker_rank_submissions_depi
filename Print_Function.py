n = int(input())

def num_of_digits(number):
    tot = 0
    while number > 0 :
        tot+=1
        number//=10
    return tot
    
ans = 1

for i in range(2 , n + 1):
    ans *= 10**(num_of_digits(i))
    ans += i
    
print(ans)
