import sys 

import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand

    
def print_color(msg):
    click.echo(click.style(msg, fg='cyan'))


def print_success(msg):
    click.echo(click.style(f'ERROR: {msg}', fg='green'))


def handle_error(msg):
    click.echo(click.style(f'ERROR: {msg}', fg='red'))
    sys.exit()
