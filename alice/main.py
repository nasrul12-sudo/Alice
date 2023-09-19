import dataBase.data as database
import brain.question as brain
import voice.speak as speak
import pentes.tools as tools
import pyfiglet as figle
import numpy
import argparse
import argparse
import os

from pentes.tools import pentes
from voice import speak

result = figle.figlet_format("Hy", font='slant')
print(result)

ghosTrack = pentes('ghos')
ghosTrack.ghostrack()

# data = pentes('https://www.vizzed.com/play/game.php%20id=%20product-item.php')
# data.sqlmap()

# test_log = os.open('/home/nasrul/.local/share/sqlmap/output/testphp.vulnweb.com/log', os.O_RDONLY)
# readByte = os.read(test_log,10000000000)
# print(readByte[-1:])