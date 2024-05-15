import click


@click.group()
def main():
    """command line interface"""
    pass

@main.command()
def hello():
    print("Hello, world!")
