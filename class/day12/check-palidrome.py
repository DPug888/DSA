string = input()
vowels="AEIOUaeiou"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count+=1
print(f"vowels:{vowel_count}")
print(f"consonants:{len(string) - vowel_count}")