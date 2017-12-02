class RoomServer(object):

    def __init__(self, num=4, isPrint=True):
        self.isPrint = isPrint
        self.memberList = []
        if self.isPrint:
            print 'Room Created'

    def loadRecord(self, recordFile):
        pass

    def checkStartable(self):
        pass

    def createGame(self):
        pass


class Game(object):

    pass