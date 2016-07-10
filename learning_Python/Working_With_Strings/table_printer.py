tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'Movie']
             ]


def printTable(table):
    colwidth = [0] * len(table)
    for i in range(len(table[0])):
        for j in range(len(table)):
            if len(table[j][i]) > colwidth[j]:
                colwidth[j] = len(table[j][i])

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colwidth[j] + 1), end=' ')
        print()


printTable(tableData)

