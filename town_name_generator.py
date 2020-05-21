import random

print("Welcome to the fantasy town name generator!\nYou can use this generator to come up with ideas for town names for stories, your Animal Crossing town, and anything else you can imagine.")

#needs a file of prefixes and a file of suffixes

# in terms of user interface I would need like a generate button 
# or i could do it all text based somehow, when they type enter??
#or maybe ask, would u like to generate yes or no then ask again? y or no
# maybe it could generate a file or some kind of pop up with the word??

#these two are just strings containing the names of the files
PREFIX_FILE_NAME = 'prefix.txt'
SUFFIX_FILE_NAME = 'suffix.txt'

def generate_name():
    return generate_prefix_or_suffix(PREFIX_FILE_NAME) + generate_prefix_or_suffix(SUFFIX_FILE_NAME)

def generate_prefix_or_suffix(file):
    read_file = open(file, 'r')
    #readlines() returns a list from read_file
    list_of_lines = read_file.readlines()
    read_file.close()
    #the strip method removes any whitespaces or newlines
    return random.choice(list_of_lines).strip()

#we only want our program to run when the user enters yes
inp = input("Would you like to generate a new name?\n").lower()
while inp == "yes" :
    print(generate_name())
    inp = input("Would you like to generate a new name?\n").lower()
