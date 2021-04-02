original = input("Enter a sentence to translate: \n").strip().lower()

# This splits the sentence and creates a list with each word
words = original.split()

new_words = []

# If it starts with a vowel: add 'yay'
# Otherwise: move the first consonant cluster
# to the end and add "ay"

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        consonants = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + consonants + "ay"
        new_words.append(new_word)

new_sentence = " ".join(new_words)
print(new_sentence)