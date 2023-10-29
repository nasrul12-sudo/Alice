import os

class pentes:
    def __init__(self,inp):
        self.inp = inp
        
    def ghostrack(self):
        os.system('python3 /mnt/USBC/pentes/GhostTrack/GhostTR.py')
        
    def burp(self):
        os.system('sudo burp')

    def sqlmap(self):
        os.system(f'sqlmap -u {self.inp} --dbs')
    
    def hydra(self):
        os.system(f'hydra ')