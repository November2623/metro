class Station:
    def __init__(self,stations):
        self._Line = stations[0]
        self._ID  = stations[1]
        self._Name = stations[2]
        self._Nbor = stations[3]
        self._Tranfer = stations[4]


    def get_station(self):
        return self._Name