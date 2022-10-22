import csv

filename = 'namesa.csv'
accessMode = 'r'

with open(filename,accessMode) as myCSVFile:
    dataCSV = csv.reader(myCSVFile,delimiter= ',')
    print(dataCSV)

    names = []
    busTypes = []
    locations = []
    results = []

    for row in dataCSV:
        name = row[0]
        busType = row
        location = row
        result = row[1]

        names.append(name)
        busTypes.append(busType)
        locations.append(location)
        results.append(result)

        print(name + ' is ' + str(result) + ' years old')