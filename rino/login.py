import click
import rinocloud
import requests
import keyring

def login(email, password):
    url = rinocloud.api_domain + '/o/token/'
    data = {
        'username': email,
        'password': password,
        'grant_type': 'password',
        'client_id': 'XIkmGK9ehXrL0At1MzADGuWcA6V7wFqtwYs7FjM7'
    }

    oauth_r = requests.post(url, data)

    if oauth_r.status_code > 400:
        click.echo(oauth_r.json()['error_description'], err=True, color='red')

    else:
        url = rinocloud.api_base + 'users/details/'
        access_token = oauth_r.json()['access_token']

        headers = {
            'Authorization': 'Bearer %s' % access_token
        }

        r = requests.post(url, headers=headers)

        if r.status_code > 400:
            click.echo(r.json()['error_description'], err=True, color='red')

        else:
            keyring.set_password('rinocloud-python-cli', 'token', r.json()['token'])
            click.echo('Logged in.')
