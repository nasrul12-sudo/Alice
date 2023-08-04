import os

class pentes:
    def __init__(self,inp):
        self.inp = inp
        
    def ghostrack(self):
        folder = os.listdir('/mnt/USBC/pentes')
        for file in folder:
            if file == 'GhostTrack':
                os.system('/mnt/USBC/pentes/GhostTrack/GhostTR.py')
            else:
                print('maaf terjadi error'); break

    def burp(self):
        os.system('sudo burp')
        
data = pentes('data')
data.burp()