from re import A


def solution(s):
    answer = ''
    length = len(s)
    
    # special case
    if (length == 1 or length == 0 or length == 2):
        answer = s
        return answer

    # even number
    elif (length % 2 == 0):
        mid_num = length // 2
        answer = s[mid_num-1:mid_num+1]
        return answer

    # odd number
    else:
        mid_num = length // 2
        answer = s[mid_num]
        return answer
