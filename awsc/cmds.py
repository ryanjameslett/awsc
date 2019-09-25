import os
import re

import click


def get_profiles():
    """
    Fetch configured AWS accounts

    Returns:
        A list of available AWS profiles
    """
    HOME = os.environ['HOME']
    accounts = []
    with open(os.path.join(HOME, '.aws/credentials')) as creds_file:
        for line in creds_file.readlines():
            if not line.startswith('['):
                continue
            accounts.append(re.match('\[(.*)\]', line).groups()[0])
    return accounts


def get_curr_profile():
    """
    Get the current AWS account

    Returns:
        string containing current AWS profile
    """
    try:
        return os.environ['AWS_PROFILE']
    except KeyError:
        return 'default'



@click.group()
def cli():
    pass


@cli.command()
def list():
    for profile in get_profiles():
        click.echo(profile)

@cli.command()
def current():
    click.echo(get_curr_profile())

if __name__ == '__main__':
    cli()
