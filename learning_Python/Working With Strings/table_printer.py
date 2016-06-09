tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'Movie']
             ]


def printTable():
    colwidth = [0] * len(tableData)
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if len(tableData[j][i]) > colwidth[j]:
                colwidth[j] = len(tableData[j][i])

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colwidth[j] + 1), end=' ')
        print()


printTable()

