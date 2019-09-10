def printsss(matrix):
    for layer in reversed(matrix):
        printss(layer)
        
def printss(matrix):
    print("\t",end="")
    for index in range(0, len(matrix[0])):
        print(index, end="\t")
    print()
    for index in range(0, len(matrix[0])):
        print("--------",end="")
    print()
    #print("\n------------------------------------------------------")
    index = 0
    for row in matrix:
        print(str(index)+"|",end="\t")
        for col in row:
            print(col, end="\t")
        index+=1
        print()
    print()
