def get_distance (target, l_pos, r_pos, hand):
    # set position
    target = str(target)
    l_pos = str(l_pos)
    r_pos = str(r_pos)
    
    pos = {
        '1' : [0, 3],
        '2' : [1, 3],
        '3' : [2, 3],
        '4' : [0, 2],
        '5' : [1, 2],
        '6' : [2, 2],
        '7' : [0, 1],
        '8' : [1, 1],
        '9' : [2, 1],
        '0' : [1, 0],
        '*' : [0, 0],
        '#' : [2, 0]
    }
    
    l_distance = abs(pos[l_pos][0] - pos[target][0]) + abs(pos[l_pos][1] - pos[target][1])
    r_distance = abs(pos[r_pos][0] - pos[target][0]) + abs(pos[r_pos][1] - pos[target][1])
    
    if (l_distance < r_distance):
        return 'L'
    if (l_distance > r_distance):
        return 'R'
    if (l_distance == r_distance):
        if (hand == "right"):
            return 'R'
        else:
            return 'L'
    
    
def solution(numbers, hand):
    answer = ''
    l_pos = '*'
    r_pos = '#'
    
    l_col = [1, 4, 7]
    r_col = [3, 6, 9]
    m_col = [2, 5, 8, 0]
    
    for n in range(0, len(numbers)):
        if (numbers[n] in l_col):
            answer = answer + 'L'
            l_pos = numbers[n]
        elif (numbers[n] in r_col):
            answer = answer + 'R'
            r_pos = numbers[n]
        else:
            # Calculate the distance
            x = get_distance(numbers[n], l_pos, r_pos, hand)
            answer = answer + x
            if x == 'L':
                l_pos = numbers[n]
            else:
                r_pos = numbers[n]
                
    return answer