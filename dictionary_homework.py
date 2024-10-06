# Exercise/Homework 1
#  Create an English to French translator program. The program takes
#    a word from the user as an input and translates it using a dictionary 
#    data type as a vocabular Please add the translation of 'prune' 
#    in your homework ®. If word is not in the code vocabulary print ((word) is 
#    not in my memory) —The user will select the language they would to 
#    translate to (optional) 
# 
# OPERATION
# # Dictionary for English to French translations
# English to French dictionary
english_to_french = {
    'apple': 'pomme',
    'banana': 'banane',
    'bread': 'pain',
    'orange': 'orange',
    'grape': 'raisin',
    'prune': 'prune',   # newly Added:  translation for 'prune'
    'sky': 'ciel',
    'yellow': 'jaune',
    'tree': 'arbre',
    'house': 'maison',
    'water': 'eau',
    'sun': 'soleil',
    'book': 'livre'
}

# Asking the user for a word he want me to translate
word_to_translate = input("Enter the word you want to translate (in English): \t")

# Asking for the language to translate to
language_choice = input("Enter the language to translate to (e.g., 'French'): \t")

# Set condition to check if the language is French
if language_choice == 'french':
    
    # Check if the word is in the dictionary
    if word_to_translate in english_to_french:
        print(f"Translation: {english_to_french[word_to_translate]}")
    else:
        print(f"'{word_to_translate}' is not in my memory.")
else:
    print("Sorry, this language is not supported by the dictionary.")
