def solution(a, b):
    answer = 0
    
    # case 1
    if (a == b):
        return a
    
    # case 2
    else:
        x = min(a, b)
        y = max(a, b)
        
        for i in range(x, y+1):
            answer += i
        
    return answer

