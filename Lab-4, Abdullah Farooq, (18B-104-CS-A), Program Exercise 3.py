print("Program Exercise 3")

word = input('Enter a word that is a palindrome: ')
word = word.casefold()
rev_word = reversed(word)
if list(word) == list(rev_word):
    print('Yes your string is a palindrome')
else:
    print('Sorry, your string is not a palindrome.')
