import os
import string
file_names = os.listdir("/Users/v/python_course/prank")
file_location = os.path.abspath("/Users/v/python_course/prank")
trantab = str.maketrans('', '', '0123456789')

def rename_files(names):
    for i in range(1,len(names)):
         #print('original file name', file_names[i], 'translated file name', file_names[i].translate(trantab))
         os.rename(file_location + '/' + file_names[i], file_location + '/' + file_names[i].translate(trantab))
         #verify changes
    print(os.listdir("/Users/v/python_course/prank"))

rename_files(file_names)
