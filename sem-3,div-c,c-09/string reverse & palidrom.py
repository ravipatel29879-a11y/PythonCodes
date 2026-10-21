def reverse_text(word):
    return word[::-1]

def check_palindrome(word):
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == reverse_text(cleaned_word)

words = ["level", "hello", "Nayan", "Surat"]

for word in words:
    reversed_word = reverse_text(word)
    palindrome_result = "Yes" if check_palindrome(word) else "No"
    print(f"String: '{word}' | Reversed: '{reversed_word}' | Palindrome: {palindrome_result}")
