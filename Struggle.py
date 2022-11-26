import subprocess

class Struggle:
    
    def __init__(self):
        self.infoHash = ''
        self.delugeStatus = ''
        self.serverSize = ''
        self.downSpeed = ''
        self.downETA = ''
        self.torrentIDs = []

    def setInfoHash(self,hash):
        self.infoHash = hash       
    
    def downloadFromHash(self):
        print(self.infoHash)

    def getMagnetFromHash(self):
        return f'magnet:?xt=urn:btih:{self.infoHash}'
    
    def getDownloadStatus(self):
        
        self.delugeStatus = ''
        self.serverSize = ''
        self.downSpeed = ''
        self.downETA = ''
        self.torrentIDs = []
    
