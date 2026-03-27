import json
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def format_json_string(data_string):
    if not data_string:
        return "{}"
    try:
        parsed = json.loads(data_string)
        return json.dumps(parsed, indent=4)
    except json.JSONDecodeError:
        return data_string
    