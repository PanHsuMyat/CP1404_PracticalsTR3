"""
CP1404 Practical 5
Word Occurrences
Estimate: 20 minutes
Actual:   37 minutes
"""

text = input("Please enter text: ")
words = text.lower().split()
word_to_count = {}

for word in words:
    word = word.strip('.,!?;:"\'')
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
print(f"Text: {text}")

unique_words = list(word_to_count.keys())
unique_words.sort()
max_word_length = max(len(word) for word in unique_words)

for word in unique_words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")