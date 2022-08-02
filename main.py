import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = {row.letter: row.code for (index, row) in data.iterrows()}

input_word = input("Enter a word: ").upper()
result = [new_data[letter] for letter in input_word]
final_result = " ".join(result)
print(final_result)
