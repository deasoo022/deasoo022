import random

def shuffle_seats(num_students, num_rows):
    # 학생 리스트 생성
    students = list(range(1, num_students + 1))
    
    # 리스트를 무작위로 섞기
    random.shuffle(students)
    
    # 학생 리스트를 줄 수에 맞게 분할
    rows = [[] for _ in range(num_rows)]
    for i in range(num_students):
        rows[i % num_rows].append(students[i])
    
    return rows

# 학생 수와 줄 수 설정
num_students = 25
num_rows = 6

# 자리 배치
seating_arrangement = shuffle_seats(num_students, num_rows)

# 결과 출력
for i, row in enumerate(seating_arrangement):
    print(f"Row {i + 1}: {row}")
