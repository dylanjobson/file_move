import os
import shutil
import glob

#source of files you want to move
source = 'YOUR PATH HERE'  

#destination for files 
destination = 'YOUR PATH HERE'  

 #extension of files you want to move
extension = '*.jpg' 

file = os.listdir(source)

for file in glob.glob(source+(extension)):
    shutil.move(file, destination) 
