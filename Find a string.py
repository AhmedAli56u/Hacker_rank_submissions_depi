def count_substring(string, sub_string):
    n = len(string)
    m = len(sub_string)
    
    ans = sum(1 for i in range(n - m + 1) if string[i:i+m] == sub_string)
    
    return ans
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
