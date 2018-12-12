import json

def save_file(name, data):
    f = open(name, encoding='utf8', mode='w')
    data = json.dumps(data)
    f.write(data)
