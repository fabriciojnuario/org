class Room:

    def __int__(self, nroom, floor, troom, status):
        self.nroom = nroom
        self.floor = floor
        self.troom = troom
        self.status = status

    def getNroom(self):
        return self.nroom

    def getFloor(self):
        return self.floor

    def getTroom(self):
        return self.troom

    def getStatus(self):
        return self.status
