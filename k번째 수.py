def work(array, param):
    temp = array[param[0]-1:param[1]]
    temp.sort()
    return temp[param[2]-1]

def solution(array, commands):
    answer = []
    
    for i in range(0, len(commands)):
        answer.append(work(array, commands[i]))
    return answer