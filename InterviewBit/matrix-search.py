"""

[+]Temporal marker           : Wed, 21:06 | Feb 05, 20
[+]Temporal marker untethered: Wed, 21:06 | Feb 05, 20
[+]Comments                  :Binary search based solution
                             *Solution devised in almost an hour
                             *Had the apporach clear
                             *Took some time to figure out the bugs
                             *Solution is accepted
                             *Matter closed for now
[+]Level                     :Easy
[+]Tread Speed               :Realaxed
[+]LINK                      : https://www.interviewbit.com/problems/matrix-search

"""


def findSolution(matrix, element):
    rows = len(matrix)
    cols = len(matrix[0])
    right = rows * cols
    left = 1

    while left <= right:
        mid = (left + right) // 2
        row = int(mid / cols)
        col = int(mid % cols) - 1
        if col == -1:
            col = cols - 1
            row -= 1
        if matrix[row][col] == element:
            return 1
        if matrix[row][col] > element:
            right = mid - 1
        else:
            left = mid + 1
    return 0


if __name__ == '__main__':
    # input_data =[matrix, search_term]
    input_data = [[[2, 3, 4, 6],
                   [16, 19, 33, 36],
                   [37, 38, 38, 41],
                   [47, 47, 50, 51],
                   [55, 57, 58, 62],
                   [63, 65, 66, 66],
                   [68, 70, 75, 77],
                   [78, 84, 84, 86],
                   [86, 87, 88, 92],
                   [94, 95, 96, 97]], 85]

    print(findSolution(input_data[0], input_data[1]))
