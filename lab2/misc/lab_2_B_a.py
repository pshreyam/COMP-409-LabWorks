with open("code.txt", "r") as f:
    content = f.read()
    characters = list(content)

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

vowel_count = 0
consonant_count = 0

for character in characters:
    if character in vowels:
        vowel_count += 1
    elif character in consonants:
        consonant_count += 1


print(f"Vowel Count: {vowel_count}")
print(f"Consonant Count: {consonant_count}")
