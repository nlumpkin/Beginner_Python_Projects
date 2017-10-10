"""
Count Words in a String – Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a 
summary.

Problem
1. how to ignore text inside triple quotes
test2 = " '''hello''' does this work "
try1 = re.findall(r'[^"{3}\w"{3}]+', test2)    
2. how to ignore variable
"""
import re


def count_words_in_string():
    try:
    #create a file object with open
        file_obj = open(input("Enter file name: "))
        print('\n')
    except FileNotFoundError:
        print("File not found.")
    #read the file into a variable. THe read() method reads a string from an open 
    #file into a variable
    data = file_obj.read()
    #close the file
    file_obj.close()
            
    #the regex method findall() returns a list
    data_list = re.findall(r"\b[\w.']+\b", data)
    #summary: file name, number of words
    print(summary(data_list, file_obj))


def summary(data_list, file_obj):
    return ("The file, '{}', contains {} individual words."\
          .format(file_obj.name, len(data_list)))
    
if __name__=='__main__':
    count_words_in_string()
    
