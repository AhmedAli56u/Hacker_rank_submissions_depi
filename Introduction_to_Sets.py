def average(array):
    st = set(array)
    return sum(n for n in st)/len(st)
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
