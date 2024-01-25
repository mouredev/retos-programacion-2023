text = "This is an example. In this text, we will count words and sentences. I hope it works!"

total_words = 0
total_words_length = 0
total_sentences = 0
longest_word = ""

inside_word = False
current_word = ""

for character in text:
    if character.isalpha() or character == "-":
        current_word += character
        inside_word = True
    else:
        if inside_word:
            total_words += 1
            total_words_length += len(current_word)

            if len(current_word) > len(longest_word):
                longest_word = current_word

            current_word = ""
            inside_word = False

    if character == ".":
        total_sentences += 1

if inside_word:
    total_words += 1
    total_words_length += len(current_word)
    if len(current_word) > len(longest_word):
        longest_word = current_word

average_word_length = total_words_length / total_words if total_words > 0 else 0

print("Total number of words:", total_words)
print("Average word length:", average_word_length)
print("Number of sentences:", total_sentences)
print("Longest word:", longest_word)
