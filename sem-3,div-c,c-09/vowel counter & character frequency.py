# Vowel Counter & Character Frequency

def find_vowels(text):
    vowel_list = "aeiouAEIOU"
    vowel_count = 0

    for letter in text:
        if letter in vowel_list:
            vowel_count += 1

    return vowel_count


# ------------------------- check occurrence of characters
def frequency_count(text):
    character_count = {}

    for letter in text:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1

    return character_count


message = "banana"

print("Sentence:", message)
print("Total Vowels:", find_vowels(message))
print("Character Frequency:", frequency_count(message))
