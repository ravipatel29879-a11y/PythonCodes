import string

# Create text file with a paragraph containing city name
text_data = (
    "Surat is a beautiful city famous for its textile industry.\n"
    "Many students come to Surat for their education and career.\n"
    "The city of Surat provides many learning opportunities."
)

with open("city_data.txt", "w") as file:
    file.write(text_data)

search_word = input("Enter a word to find its frequency: ").strip()

with open("city_data.txt", "r") as file:
    content_lines = file.readlines()

line_count = len(content_lines)
character_count = sum(len(line) for line in content_lines)

complete_text = "".join(content_lines)
word_list = complete_text.translate(
    str.maketrans("", "", string.punctuation)
).lower().split()

word_total = len(word_list)
frequency = word_list.count(search_word.lower())

print(f"\nTotal Number of Lines: {line_count}")
print(f"Total Number of Words: {word_total}")
print(f"Total Number of Characters: {character_count}")
print(f"Frequency of '{search_word}': {frequency}")