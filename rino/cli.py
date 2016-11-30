import click
import rino

@click.group()
def cli():
    pass

@cli.command()
def init():
    """
        Initializes a rino repo.
    """
    rino.initialize.initialize()

@cli.command()
@click.option('--email', prompt='Your Rinocloud login email')
@click.option('--password', prompt='Your Rinocloud password [hidden]', hide_input=True)
def login(email, password):
    """
        Logs user in and saves api token in machine keyring.
    """
    rino.login.login(email, password)

@cli.group()
def remote():
    """
        Holds commands for setting the remote target path on Rinocloud
    """
    pass

@remote.command()
@click.argument('path', type=click.Path())
def set(path):
    """
        Set the remote target Rinocloud path
    """
    rino.remote.set(path)

@remote.command()
def unset():
    """
        Unset the remote target Rinocloud path
    """
    rino.remote.unset()

@remote.command()
def list():
    """
        List the remote target Rinocloud path
    """
    rino.remote.list()

@cli.group()
def notebook():
    """
        Holds commands for pushing notebooks
    """
    pass

@notebook.command()
@click.argument('file', type=click.Path())
def push(file):
    """
        Push the notebook
    """
    rino.notebook.push(file)

@notebook.command()
@click.argument('file', type=click.Path())
def update(file):
    """
        Push the notebook
    """
    rino.notebook.update(file)
