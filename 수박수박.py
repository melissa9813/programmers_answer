def solution(n):
    answer = ''
    str = ["수", "박"]
    
    for i in range(n):
        answer += str[i%2]
    return answer