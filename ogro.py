original = input("Enter a sentence to translate: \n").strip().lower()

words = original.split()

new_words = []

for word in words:
    if word[len(word) - 1] == "o":
        new_word = word + "gro"
        new_words.append(new_word)
    else:
        new_words.append(word)

new_sentence = " ".join(new_words)
print(new_sentence)