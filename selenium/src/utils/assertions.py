import json
from os.path import join, dirname
from jsonschema import validate


schemas_folder = 'schemas'

def validate_schema(data, schema_file):
    """Checks whether the given data matches the schema"""
    schema = _load_json_schema(schema_file)
    return validate(data, schema)

def _load_json_schema(file_name):
    """Loads the given schema file"""
    parent_dir = dirname(dirname(__file__))
    absolute_path = join(parent_dir, schemas_folder, file_name)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
