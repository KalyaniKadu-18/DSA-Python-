word = 'Kalyani'
vowels = "aeiou"

for i in range(len(word)):
    if word[i] in vowels:
        result = word[i:] + word[:i] + "ay"
        print("Result:", result)
        break