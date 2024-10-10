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

# Reverse dictionary for French to English translation
french_to_english = {v: k for k, v in english_to_french.items()}  # other way to write this is :french_to_english = {french_word: english_word for english_word, french_word in english_to_french.items()}


# Asking the user for a word they want to translate
word_to_translate = input("Enter the word you want to translate (English or French): \t").lower()

# Translation logic based on input word
if word_to_translate in english_to_french:
    # If the word is in the English-to-French dictionary
    print(f"Translation in French: {english_to_french[word_to_translate]}")
    
elif word_to_translate in french_to_english:
    # If the word is in the French-to-English dictionary
    print(f"Translation in English: {french_to_english[word_to_translate]}")
    
else:
    print(f"'{word_to_translate}' is not in my dictionary.")