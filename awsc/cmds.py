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
    return sorted(accounts)


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


def set_profile(profile):
    """
    Set the aws profile to a new value

    Args:
        profile (str): The name of the profile to set
    """
    curr_shell = '/usr/bin/zsh'
    os.system(f'{curr_shell} -c \'echo "export AWS_PROFILE={profile}\nrm -f ./update_profile.sh" > ./update_profile.sh\'')
    click.echo("Run the following command:")
    click.echo("source ./update_profile.sh")


@click.group()
def cli():
    pass


@cli.command()
def list(help='write list of available aws profiles'):
    for idx, profile in enumerate(get_profiles()):
        click.echo(f'[{idx+1}] {profile}')


@cli.command()
def curr(help='Show currently selected profile'):
    profiles = get_profiles()
    current = get_curr_profile()
    validity = ' [INVALID]' if current not in profiles else ''
    click.echo(f'{current}{validity}')


@cli.command()
@click.argument('profile_num', nargs=1, type=click.INT)
def set(profile_num, help='Set the profile to the given profile number'):
    profile = get_profiles()[profile_num - 1]
    set_profile(profile)

if __name__ == '__main__':
    cli()
