# 3.6 Word Frequency Counter
import re

sentence = """
Java is a popular programming language. Java is powerful, simple,
and java code is easy and readable.
"""

# Clean and tokenize words
word_list = re.findall(r'\b\w+\b', sentence.lower())

# Count frequency
word_count = {}
for item in word_list:
    word_count[item] = word_count.get(item, 0) + 1

# Sort by frequency (most common first)
frequency_list = sorted(word_count.items(), key=lambda element: element[1], reverse=True)

print(f"{'Word':<15} | {'Count':<10}")
print("-" * 28)
for item, total in frequency_list:
    print(f"{item:<15} | {total:<10}")
