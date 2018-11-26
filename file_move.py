import os
import shutil
import glob

source = 'YOUR PATH HERE'  #source of files you want to move
destination = 'YOUR PATH HERE'  #destination for files 
extension = '*.jpg'  #extension of files you want to move
files = os.listdir(source)


for file in glob.glob(source+(extension)):
    shutil.move(file, destination) 
