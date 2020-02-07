"""

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

[+]Temporal marker           : Thu, 10:38 | Feb 06, 20
[+]Temporal marker untethered: Thu, 10:45 | Feb 06, 20
[+]Comments                  :new the apporach
                             *solution is accepted
                             *Matter is fully closed now, pushing the solution now.
[+]Level                     :easy
[+]Tread Speed               :paced
[+]LINK                      : https://www.interviewbit.com/problems/sorted-insert-position

"""


def searchInsert(array, element):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            right = mid - 1
        else:
            left = mid + 1
    print("array[mid]: "+str(array[mid])+" mid: "+str(mid))
    if array[mid] > element:
        return mid
    return mid + 1


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    pass


if __name__ == '__main__':
    obj = Solution()
    array = [
        [3, 4, 18, 19, 20, 27, 28, 31, 36, 42, 44, 71, 72, 75, 82, 86, 88, 97, 100, 103, 105, 107, 110, 116, 118, 119,
         121, 122, 140, 141, 142, 155, 157, 166, 176, 184, 190, 199, 201, 210, 212, 220, 225, 234, 235, 236, 238, 244,
         259, 265, 266, 280, 283, 285, 293, 299, 309, 312, 317, 335, 341, 352, 354, 360, 365, 368, 370, 379, 386, 391,
         400, 405, 410, 414, 416, 428, 433, 437, 438, 445, 453, 457, 458, 472, 476, 480, 485, 489, 491, 493, 501, 502,
         505, 510, 511, 520, 526, 535, 557, 574, 593, 595, 604, 605, 612, 629, 632, 633, 634, 642, 647, 653, 654, 656,
         658, 686, 689, 690, 691, 709, 716, 717, 737, 738, 746, 759, 765, 775, 778, 783, 786, 787, 791, 797, 801, 806,
         815, 820, 822, 823, 832, 839, 841, 847, 859, 873, 877, 880, 886, 904, 909, 911, 917, 919, 937, 946, 948, 951,
         961, 971, 979, 980, 986, 993], 902]
    print(searchInsert(array[0], array[1]))
