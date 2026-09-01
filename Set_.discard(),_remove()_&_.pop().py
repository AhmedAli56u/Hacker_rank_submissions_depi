n = int(input())
st = set(map(int, input().split()))  

com = int(input())

for i in range(com):
    s = input()
    
    if s == 'pop':
        st.pop()
    else:
        s = list(s.split())
        num = int(s[1])
        s = s[0]
        if s == 'remove':
            st.remove(num)
        elif s == 'discard':
            st.discard(num)
            
            
print(sum(st))
