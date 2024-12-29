vowels={'a':'vowel','e':'vowel','i':'vowel','o':'vowel','u':'vowel','A':'vowel','E':'vowel','I':'vowel','O':'vowel','U':'vowel'}
char=input('Enter a character:')
if char in vowels:
    print(char, 'is',vowels[char])
else:
    print('Not a vowel')
