'''

[+]Temporal marker           : 1734 Hours | Friday 27, 2020
[+]Temporal marker untethered: 1752 Hours | Friday 27, 2020
[+]Comments                  : solved in 20 minutes, optimized experimental approach also devised
                                >>Matter is closed now.
[+]Space Complexity          : O(2^N)
[+]Time Complexity           : O(2^N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Paced
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''
# 17 3405:52
#A
def permute(lis):
    frontier, solution = [([], lis)], set()
    while frontier:
        list_till_now, list_left = frontier.pop()
        if not list_left:
            solution.add(tuple(list_till_now))
            continue
        for index in range(len(list_left)):
            frontier.append((list_till_now + [list_left[index]],
                             list_left[:index] + list_left[index + 1:]
                             )
                            )
    return sorted(solution)

#ACCEPTED
def permute_experimental(lis):
    def driver(index, new_list, solution):
        solution.add(tuple(new_list))

        if index == len(new_list)-1:
            solution.add(tuple(new_list))
            return

        for i in range(index, len(new_list)-1):
            for j in range(i+1, len(new_list)):
                new_list[i], new_list[j] = new_list[j], new_list[i]
                driver(i + 1, new_list, solution)
                new_list[i], new_list[j] = new_list[j], new_list[i]

    solution = set()
    driver(0, lis,solution)
    return sorted(solution)


if __name__ == '__main__':
    print(permute_experimental([1,2,3]))