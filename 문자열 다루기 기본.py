def solution(s):
    answer = False
    length = len(s)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    if (length == 4 or length == 6):
        for i in s:
            if (i not in numbers):
                return answer
        answer = True
        return answer
    
    return answer
