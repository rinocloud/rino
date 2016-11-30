from rino import config
import click
import json
import os


def initialize():
    cwd = os.getcwd()

    dir_path = os.path.join(cwd, '.rino')
    hook_path = os.path.join(dir_path, 'hooks')
    config_path = os.path.join(dir_path, 'config.json')

    exists_already = os.path.isdir(dir_path)

    if not exists_already:
        os.mkdir(dir_path)

    if not os.path.isdir(hook_path):
        os.mkdir(hook_path)

    if not os.path.exists(config_path):
        with open(config_path, 'w') as outfile:
            outfile.write(json.dumps(config.default_config))

    if exists_already:
        click.echo('Reinitialized rino repo in %s' % cwd)
    else:
        click.echo('Initialized rino repo in %s' % cwd)
