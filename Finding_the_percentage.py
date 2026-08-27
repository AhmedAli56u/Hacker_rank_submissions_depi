if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    n = len(student_marks[query_name])
    tot = 0
    
    for x in student_marks[query_name]:
        tot += x
    
    print(f"{tot/n:.2f}")
