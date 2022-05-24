def solution(arr, divisor):
    answer = []
    count = 0
    
    for i in range(0, len(arr)):
        if ((arr[i] % divisor) == 0):
            answer.append(arr[i])
            count += 1
    
    
    if (count == 0):
        answer = [-1]
        return answer
    
    else:
        answer.sort()
        return answer
