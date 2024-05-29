import codecs
import json


def write_json(data, file_path):
    with codecs.open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file)
