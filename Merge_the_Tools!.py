def merge_the_tools(string, k):
    n = len(string)//k
    for i in range(n):
        word = []
        for j in range(k*i , i*k + k):
            if string[j] not in word:
                word.append(string[j])
        print("".join(word))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
