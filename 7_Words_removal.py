import re

text = "się, i, oraz, nigdy, dlaczego, się, i, oraz, nigdy, dlaczego, usunięte"

words_to_delete = ["się", "i", "oraz", "dlaczego", "nigdy"]

splited_text = text.split()

result = [word for word in re.split("\W+",text) if word.lower() not in words_to_delete]
print(' '.join(result))