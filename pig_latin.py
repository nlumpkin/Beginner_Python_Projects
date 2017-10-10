"""
Pig Latin  Pig Latin is a game of alterations played on the English language 
game. To create the Pig Latin form of an English word the initial consonant 
sound is transposed to the end of the word and an ay is affixed 
(Ex.: "banana" would yield anana-bay).
"""
import string

def pig_latin():
    #input a single word
    word = input("Enter a word for Pig Latin translation. ").lower()
    
    punctuation = string.punctuation
    word = ''.join(char for char in word if char not in punctuation)
    #if the first letter isnt 'aeiou' stick it at the end of the word: hyphen +
    #consonant + ay 
    vowels = 'aeiou'
    if word[0] not in vowels:
        print(word[1:] +"-"+word[0]+"ay")
    else:
        print(word +"-"+word[0]+"ay")
        
if __name__=='__main__':
    pig_latin()