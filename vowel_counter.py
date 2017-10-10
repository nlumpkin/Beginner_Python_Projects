"""
Count Vowels – Enter a string and the program counts the number of vowels in 
the text. For added complexity have it report a sum of each vowel found.
"""

def vowel_counter(word):
    #list the vowels
    vowels = 'aeiou'
    #set up a count variable
    #loop over the word
    #if a char in the word is in the vowels var increment count var
    count_list = [char for char in word if char in vowels]
    count = len(count_list)
    #add char to a dictionary
    letter_dict = {}
    for char in word:
        if char in vowels:
            if not char in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
    #return count
    return count, letter_dict