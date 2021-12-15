import re

text = "się, i, oraz, nigdy, dlaczego, się, i, oraz, nigdy, dlaczego, usunięte"

words_to_delete = ["się", "i", "oraz", "dlaczego", "nigdy"]

replace_words = {
    'i': 'oraz',
    'nigdy': 'prawie nigdy',
    'dlaczego': 'czemu'
}

result = []
for word in re.split("\W+",text):
    if word in replace_words.keys():
        result.append(replace_words[word])
    else:
        result.append(word)

replaced_words = " ".join(result)
print(replaced_words)
