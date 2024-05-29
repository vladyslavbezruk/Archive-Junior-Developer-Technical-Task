import json
import os
import unittest

from json_func import write_json


class TestWriteJson(unittest.TestCase):

    def test_write_json(self):
        data = [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]

        temp_file_path = "test_data.json"

        write_json(data, temp_file_path)

        self.assertTrue(os.path.exists(temp_file_path))

        with open(temp_file_path, 'r') as file:
            loaded_data = json.load(file)
            self.assertEqual(data, loaded_data)

        os.remove(temp_file_path)


if __name__ == '__main__':
    unittest.main()
