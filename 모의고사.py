def solution(answers):
    answer = []
    grades = []

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1 = 0
    score2 = 0
    score3 = 0


    # check answers
    for i in range(0, len(answers)):
        if (answers[i] == student1[i % len(student1)]):
            score1 += 1
        if (answers[i] == student2[i % len(student2)]):
            score2 += 1
        if (answers[i] == student3[i % len(student3)]):
            score3 += 1

    grades.append(score1)
    grades.append(score2)
    grades.append(score3)

    # find the highest score
    max_score = max(grades)

    for i in range(0, len(grades)):
        if (grades[i] == max_score):
            answer.append(i+1) 
    
    return answer

a = [1,3,2,4,2]
print(solution(a))