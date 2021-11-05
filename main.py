from shutil import copytree, ignore_patterns
import json


with open('params.json', 'r') as f:
    json_dict = json.loads(f.read())

source = json_dict.get('source_folder')
destination = json_dict.get('destination_folder')
ignore = json_dict.get('ignore_patterns')


if __name__ == "__main__":
    copytree(source, destination, ignore=ignore_patterns(*ignore), dirs_exist_ok=True)
