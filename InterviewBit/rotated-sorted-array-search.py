"""

[+]Temporal marker           : Sat, 10:39 | Feb 08, 20
[+]Temporal marker untethered: Sat, 13:49 | Feb 08, 20
[+]Comments                  : WOhooooooooo!!!!!!!!!!!!! this question sucked
                             *I found the working & the actual approach around an Hour give or take
                             *Literally, eversince i'm engaged in full time bugfixing, literally adding validations
                             for each failed test case. God! i need to work on my skills
                             *At the very least, the solution is working now abosolutely fine and is accepted!
                             *I can rest now
                             *for the temporal marker, Watched one hour episode, Did laundry TWICE
                             *Would create much more cleaner & efficient solution soon

[+]Level                     :MEDIUM
[+]Tread Speed               :Relaxed  | Paced
[+]LINK                      : https://www.interviewbit.com/problems/rotated-sorted-array-search

"""


def binarySearch(arrays, element):
    print('searching for...' + str(element) + ' in >> ' + str(arrays))
    left = 0
    right = len(arrays) - 1
    while left <= right:
        mid = (left + right) // 2
        if arrays[mid] == element:
            print(str(element) + ' is found at: ' + str(mid))
            return mid
        elif arrays[mid] > element:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def findSolution(arrays, element):
    pivot = findPivot(arrays)
    print('pivot found at position...' + str(pivot) + ' >> ' + str(arrays[pivot]))
    if arrays[pivot] == element:
        return pivot
    elif element > arrays[len(arrays) - 1]:
        print('inside first half..')
        return binarySearch(arrays[:pivot + 1], element)
    else:
        print('inside second half...')
        temp = binarySearch(arrays[pivot:], element)
        if temp != -1:
            temp += pivot
        return temp


def findPivot(arrays):
    length = len(arrays)
    left = 0
    right = length - 1
    while left <= right:
        print('left: ' + str(left) + ' right: ' + str(right))
        mid = (left + right) // 2
        if arrays[mid] < arrays[mid - 1] and arrays[mid] < arrays[mid + 1]:
            print('returning mid: ' + str(mid))
            return mid
        elif arrays[mid] < arrays[left]:
            right = mid
        elif arrays[mid] > arrays[right]:
            if right == length - 1 and abs(left - right) == 1:
                return right
            else:
                left = mid
        else:
            return 0
    return -1

array = [180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9,
         10, 14,
         16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64,
         67, 69,
         72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111,
         113, 115,
         116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155,
         156, 160,
         162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177]
array = [101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100]
array = [101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100]
array = [1, 7, 67, 133, 178]
array = [19, 20, 21, 22, 28, 29, 32, 36, 39, 40, 41, 42, 43, 45, 48, 49, 51, 54, 55, 56, 58, 60, 61, 62, 65, 67, 69, 71,
         72, 74, 75, 78, 81, 84, 85, 87, 89, 92, 94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 109, 110, 112, 113, 115,
         117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 131, 133, 134, 135, 136, 137, 138, 139, 141, 142,
         144, 146, 147, 148, 149, 150, 153, 155, 157, 159, 161, 163, 164, 169, 170, 175, 176, 179, 180, 185, 187, 188,
         189, 192, 196, 199, 201, 203, 205, 3, 7, 9, 10, 12, 13, 17]
array = [180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9,
         10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62,
         63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107,
         108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144,
         145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177]

print("searching pivot for lis: " + str(array))
print(findSolution(array, 42))
