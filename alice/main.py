import dataBase.data as DB
import brain.question as q
import sys      
import time
import platform
import os
import click
import argparse
import pyfiglet as figle
import argparse

print("hay broder")

result = figle.figlet_format("Hy", font='slant')
print(result)

parser = argparse.ArgumentParser(description='jus an alice', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-a", "--archiver", action='store_true', help='archive mode')
args = parser.parse_args()
config = vars(args)
print(config)