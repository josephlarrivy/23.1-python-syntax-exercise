# For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words (words):
    for word in words:
        print(word.upper())

def print_start_e (words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_start_with (words, letter):
    for word in words:
        if word.startswith(letter) or word.startswith(letter.upper()):
            print(word.upper())
            break