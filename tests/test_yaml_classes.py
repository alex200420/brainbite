import unittest
import os
from tempfile import NamedTemporaryFile
from brainbite.yaml_classes import YAML_Handler

class TestYAMLHandler(unittest.TestCase):

    def setUp(self):
        self.yaml_str = '''
        info:
            name: "Alice"
            age: 30
        '''
        self.yaml_file = NamedTemporaryFile(mode='w', delete=False)
        self.yaml_file.write(self.yaml_str)
        self.yaml_file.close()
        self.yaml_handler = YAML_Handler(self.yaml_file.name)

    def tearDown(self):
        os.unlink(self.yaml_file.name)

    def test_load_yaml_file(self):
        yaml_dict = self.yaml_handler.load_yaml_file(self.yaml_file.name)
        self.assertEqual(yaml_dict, {'info': {'name': 'Alice', 'age': 30}})

    def test_get_yaml_unpacked(self):
        person = self.yaml_handler.get_yaml_unpacked('info')
        self.assertEqual(person.name, 'Alice')
        self.assertEqual(person.age, 30)

if __name__ == '__main__':
    unittest.main()
