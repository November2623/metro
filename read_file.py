import csv
from stations import Station
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
        elif 'START' in list_stations[temp] or len(list_stations[temp])== 0:
            flag =  False
        else:
            list1 = []
            list1.append(key)
            if 'Conn' not in list_stations[temp]:
                station  = list_stations[temp].split(':')
                for i in station:
                    list1.append(i)
                if len(list_stations[temp + 1]) == 0:
                    list1.append('End')
                elif '#' not in list_stations[temp + 1]:
                    list1.append(list_stations[temp + 1])
                else:
                    list1.append('End')
                list1.append('None')
            else:
                index = list_stations[temp].split(':Conn:')
                m_index = index[0].split(':')
                for i in m_index:
                    list1.append(i)
                if len(list_stations[temp + 1]) == 0:
                    list1.append('End')
                elif '#' not in list_stations[temp + 1]:
                    list1.append(list_stations[temp + 1])
                else:
                    list1.append('End')
                list1.append(index[1])
            list.append(list1)
        temp += 1
    all_stations = [Station(i) for i in list]
    for i in all_stations:
        print(i._Tranfer)
        
read_file()