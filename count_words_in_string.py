"""
Count Words in a String – Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a 
summary.
"""

import re

#create a file object with open
file_obj = open('this_is_how_we_do_it.txt')
#read the file into a variable. THe read() method reads a string from an open 
#file into a variable
data = file_obj.read()
#close the file
file_obj.close()
        
#the regex method findall() returns a list
data_list = re.findall(r"\b[\w.']+\b", data)
#summary: file name, number of words
def summary(data_list, file_obj):
    print("The file, '{}', contains {} individual words."\
          .format(file_obj.name, len(data_list)))