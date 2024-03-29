'''student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
'''
import pandas
import csv
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(dict)
def exception():
    name = input("What is your name? ").upper()

    try:
        output = [dict[letter] for letter in name]
    except KeyError:
        print("Sorry! Enter an alphanumeric letter.")
        exception()
    else:
        print(output)
exception()


