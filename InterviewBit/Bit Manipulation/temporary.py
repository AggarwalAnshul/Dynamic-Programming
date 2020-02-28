def findSolution(painters, time, boards):
    def isPossible(painters, time, boards):
        painter = 0
        temp = 0
        for board in boards:
            if board > time:
                return False
            elif temp + board > time:
                painter += 1
                temp = board
            else:
                temp += board
        if painter > painters:
            return False
        return True

    total = 0
    for board in boards:
        total += board
    if painters == 1:
        return total * time

    left = 0
    right = total
    while left <= right:
        mid = (left + right)//2
        if isPossible(painters, mid, boards):
            right = mid - 1
        else:
            left = mid + 1
    return (right + 1)*time

if __name__ == '__main__':
    print(findSolution(5, 10, [ 658, 786, 531, 47, 169, 397, 914]))
    print(findSolution(2, 5, [1, 10]))
    print(findSolution(1, 5, [1, 10]))
    print(findSolution(10, 1, [1, 8, 11, 3]))
