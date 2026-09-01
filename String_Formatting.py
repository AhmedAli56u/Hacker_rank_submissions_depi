def print_formatted(number):
    n = len(str(f"{number:b}")) 
    
    for i in range(1 , number + 1):
        print(f"{i}".rjust(n), f"{i:o}".rjust(n), f"{i:X}".rjust(n), f"{i:b}".rjust(n))

n = int(input())
print_formatted(n)
