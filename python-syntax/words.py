def print_upper_words(words, letters):
    for word in words:
        if word[0].lower() in letters:
            print(word.upper())

words = ["apple", "banana", "grape", "cherry"]
letters = {'a', 'e'}
print_upper_words(words, letters)
