def print_rangoli(size):
    chars = []
    lne = 4*size - 3
    for i in range(size):
        chars.append(chr(ord('a') + i))
        
    stores = []
    
    for i in range(size):
        new_lis = chars[-1:-2-i:-1] + chars[size -i: size]
        store = '-'.join(new_lis)
        print(store.center(lne,'-'))
        
        if i < size - 1:
            stores.append(store.center(lne,'-'))
            
    for i in range(len(stores)):
        print(stores[len(stores) - i - 1])
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
