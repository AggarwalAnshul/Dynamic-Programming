def printsss(matrix):
    for layer in reversed(matrix):
        printss(layer)
        
def printss(matrix, string , rev):
    temp = [0]
    for x in string:
        temp.append(x)
    string = temp
    print("\t",end="")
    for index in string:
        print(index, end="\t")
    print()
    for index in range(0, len(matrix[0])):
        print("--------",end="")
    print()
    #print("\n------------------------------------------------------")
    index = 0
    rev = "0"+rev
    for row in matrix:
        print(str(rev[index])+"|",end="\t")
        for col in row:
            print(col, end="\t")
        index+=1
        print()
    print()
