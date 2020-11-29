#词汇表
word_lists = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    }

word = 'string'
print(f"{word.title()}: {word_lists[word]}")

word = 'comment'
print(f"{word.title()}: {word_lists[word]}")

word = 'list'
print(f"{word.title()}: {word_lists[word]}")

word = 'loop'
print(f"{word.title()}: {word_lists[word]}")

word = 'dictionary'
print(f"{word.title()}: {word_lists[word]}")
