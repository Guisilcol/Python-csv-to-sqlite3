import json

def get_config_dict() -> dict:
    with open('config.json', 'r') as f:
        return json.load(f)