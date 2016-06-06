tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if len(tableData[j][i]) > colWidths[j]:
                colWidths[j] = len(tableData[j][i])
    print(colWidths)

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y] + 1), end='')
        print()



printTable()
