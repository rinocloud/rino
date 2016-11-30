import click
import json
import os

default_config = {}

def set(key, val):
    cwd = os.getcwd()
    dir_path = os.path.join(cwd, '.rino')
    config_path = os.path.join(dir_path, 'config.json')

    if not os.path.isdir(dir_path):
        click.echo('Not a rino repository.')
        return False

    if not os.path.exists(config_path):
        with open(config_path, 'w') as outfile:
            outfile.write(json.dumps(config.default_config))
            return False

    else:
        conf = json.loads(open(config_path, 'r').read())
        conf[key] = val
        with open(config_path, 'w') as outfile:
            outfile.write(json.dumps(conf))
        return True


def get(key):
    cwd = os.getcwd()
    dir_path = os.path.join(cwd, '.rino')
    config_path = os.path.join(dir_path, 'config.json')

    if not os.path.isdir(dir_path):
        click.echo('Not a rino repository.')
        return False

    if not os.path.exists(config_path):
        return None

    else:
        conf = json.loads(open(config_path, 'r').read())
        if key in conf:
            return conf[key]
        else:
            return False
