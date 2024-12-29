nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled) 
words = ["apple", "banana", "cherry"]
uppercase_words = list(map(lambda x: x.upper(), words))
print(uppercase_words)  
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  
words = ["cat", "elephant", "dog", "fox"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)  
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x + y, nums)
print(product) 
from functools import reduce

words = ["cat", "elephant", "dog", "rhinoceros"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest_word)  