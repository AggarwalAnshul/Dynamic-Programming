"""

[+]Temporal marker           : Wed, 22:34 | Feb 05, 20
[+]Temporal marker untethered: Wed, 22:34 | Feb 05, 20
[+]Comments                  :
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/search-for-a-range

"""


class Solution:
    def searchRange(self, array, element, dir, left, right):
        ans = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if array[mid] > element:
                right = mid - 1
            elif array[mid] < element:
                left = mid + 1
            elif(dir==0):
                temp = self.searchRange(array, element, 1, left, mid - 1)
                if temp != -1:
                    ans[0] = temp
                temp = self.searchRange(array, element, 2, mid + 1, right)
                if temp != -1:
                    ans[1] = temp
                return ans
            elif dir == 1:
                temp = self.searchRange(array, element, dir, left, mid - 1)
                if temp != -1:
                    return temp
                else:
                    return mid
                return -1
            else:
                # direction is 2
                while left <= right:
                    mid = (left + right) // 2
                    if array[mid] > element:
                        right = mid - 1
                    elif array[mid] < element:
                        left = mid + 1
                    else:
                        temp = self.searchRange(array, element, dir, mid + 1, right)
                        if temp != -1:
                            return temp
                        return mid
                return -1
        return ans


'''
def searchRight(array_Right, element_Right, left_Right):
    print("searching in right side...")
    print(array_Right)
    right_Right = len(array_Right) - 1
    while left_Right <= right_Right:
        mid_Right = (left_Right + right_Right) // 2
        if array_Right[mid_Right] == element_Right:
            temp = searchRight(array_Right, element_Right, mid_Right + 1)
            if temp != -1:
                print('returning:' + str(temp))
                return temp
            else:
                return mid_Right
        if array_Right[mid_Right] > element_Right:
            right_Right = mid_Right - 1
        else:
            left_Right = mid_Right - 1
    print("returning -1...")
    return -1


def searchLeft(array_left, element_left):
    print("searching in left side...")
    print(array_left)
    left_left = 0
    right_left = len(array_left) - 1
    while left_left <= right_left:
        mid_left = (left_left + right_left) // 2
        if array_left[mid_left] == element_left:
            temp = searchLeft(array_left[0:mid_left], element_left)
            if temp != -1:
                return temp
            else:
                return mid_left
        if array_left[mid_left] > element_left:
            right_left = mid_left - 1
        else:
            left_left = mid_left + 1
    return -1


def searchRange(array, element):
    left = 0
    right = len(array) - 1
    print("left: " + str(left) + " right: " + str(right))
    print('searching for: ' + str(element))
    while left <= right:
        mid = (left + right) // 2
        print('mid: '+str(mid))
        if array[mid] > element:
            print('mid is greater...')
            right = mid - 1
        elif array[mid] < element:
            print("mid is lesser...")
            left = mid + 1
        else:
            # checking on the left side
            ans = [mid, mid]
            print("middle found..." + str(mid))
            leftSide = searchLeft(array[0:mid], element)
            print("leftSide: " + str(leftSide))
            rightSide = searchRight(array, element, mid + 1)
            print("rightSide: " + str(rightSide))
            if leftSide != -1:
                ans[0] = leftSide
            if rightSide != -1:
                ans[1] = rightSide
            return ans
    return [-1, -1]
'''

if __name__ == '__main__':
    obj = Solution()
    data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
         4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
         4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
         6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
         6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
         7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
         8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
         9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
         9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
         10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 128]
    data = [[1], 1]

    print(obj.searchRange(data[0], data[1], 0, 0, len(data[0]) - 1))
