import nltk

nltk.download('averaged_perceptron_tagger')


def determine_pos(word):
    pos_tags = nltk.pos_tag([word])
    return pos_tags[0][1]

# Пример использования функции
word = "apologise"
pos = determine_pos(word)
print("Часть речи для слова '{}' - {}".format(word, pos))
