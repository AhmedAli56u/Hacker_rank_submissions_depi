def minion_game(string):
    n = len(string)
    vowels = ['A','a','E','e','O','o','I','i','U','u']
    
    kev = 0
    stu = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kev += len(string) - i
        else:
            stu += len(string) - i
            
            
    if kev > stu:
        print(f"Kevin {kev}")
    elif kev < stu:
        print(f"Stuart {stu}")
    else:
        print("Draw")
    
                

if __name__ == '__main__':
    s = input()
    minion_game(s)
