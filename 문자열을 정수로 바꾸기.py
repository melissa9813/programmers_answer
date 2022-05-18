def solution(s):
    answer = 0
    
    # negative
    if s[0] == "-":
        new_s = s[1:]
        answer = int(new_s) * -1
        
    # positive
    else:
        answer = int(s)
        
    return answer
