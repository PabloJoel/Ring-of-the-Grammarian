import os
import json

project_path = os.getcwd()  # Path of the project
json_path = os.path.join(project_path, 'raw_english_dictionary.json')

with open(json_path, 'r') as json_file:
    json_dict = json.load(json_file)

new_json = dict()
for key in json_dict:
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

with open('processed_english_dictionary.json', 'w') as json_write:
    json_object = json.dumps(new_json, indent=4)
    json_write.write(json_object)
