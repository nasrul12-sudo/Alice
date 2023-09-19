import numpy as np
import os
import tensorflow as tf

from PIL import Image 

def trainImg(folder):
    print(folder)
    path = os.listdir(folder)
    
    image = []
    for i in range(len(path)):
        print(i, " : ", path[i])
        img = path[i]
        image.append(img)
        
    inp = int(input(">> "))
    # print(image)
    img_opn = Image.open(image[inp])
    img_arr = np.array(img_opn)
    
    for i in range(len(img_arr)):
        print(img_arr[i])

train = os.listdir('/home/nasrul/Documents/GitHub/Alice/alice/brain/image/train')
test = os.listdir('/home/nasrul/Documents/GitHub/Alice/alice/brain/image/test')

for i in range(len(train)):
    d = train[i]
    print(i, " : ", d)

inp = int(input(">> "))

os.chdir(f"/home/nasrul/Documents/GitHub/Alice/alice/brain/image/train/{train[inp]}")
path = (os.getcwd())

trainImg(path)
# arr_img = Image.open(r"/home/nasrul/Documents/GitHub/Alice/alice/brain/image/train/character_6_cha/75782.png")
# d_arr = np.array(arr_img)
# for i in range(len(d_arr)):
#     print(d_arr[i])
    # for j in range(len(d_arr)):
    #   print(d_arr[i][j])  
