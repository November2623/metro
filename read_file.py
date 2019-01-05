import csv
from stations import station
def read_file():
    list_stations = []
    with open('delhi-metro-stations') as csvfile:
        contents = csv.reader(csvfile)
        for i in contents:
            list_stations.append(''.join(i))
    temp  = 0
    key = ' '
    list = []
    flag = True
    while flag:
        if '#' in list_stations[temp]:
            key  = list_stations[temp]
        elif 'START' in list_stations[temp]:
            flag =  False
        else:
            list1 = []
            list1.append(key)
            station  = list_stations[temp].split(':')
            for i in station:
                list1.append(i)
            list.append(list1)
        temp += 1
    for i in list:
        print(i)
read_file()