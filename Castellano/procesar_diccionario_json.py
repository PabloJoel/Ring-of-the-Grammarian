import os
import json

project_path = os.getcwd()  # Path of the project
dictionary_path = os.path.join(project_path, 'diccionario_sin_procesar.txt')

with open(dictionary_path, 'r', encoding='utf-8') as read_file:
    content = read_file.read().splitlines()

new_json = dict()
for key in content:
    word = key.lower()
    first_letter = word[0]
    word_size = len(word)

    if '-' != first_letter:
        if first_letter in new_json and word_size in new_json[first_letter]:
            new_json[first_letter][word_size].append(word)
        elif first_letter in new_json:
            new_json[first_letter].update({word_size: [word]})
        else:
            new_json.update({first_letter: {word_size: [word]}})

with open('diccionario_procesado.json', 'w', encoding='utf-8') as json_write:
    json_object = json.dumps(new_json, indent=4, ensure_ascii=False)
    json_write.write(json_object)
