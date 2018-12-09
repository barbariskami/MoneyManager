import os, json


def open_file(name):
    if not os.path.exists(name):
        data = {'Sum': 0, 'Operations': [], 'Payments': []}
    else:
        f = open(name, encoding='utf8').read()
        data = json.loads(f)
    return data


