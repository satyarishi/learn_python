student = []
second_student = []
marks = set()
for _ in range(int(input())):
    name = input()
    score = float(input())
    student.append([name,score])
    marks.add(score)

sg = sorted(marks)[1]

for name,score in student:
    if score == sg:
        second_student.append(name)
second_student.sort()
for name in second_student:
    print(name)      

