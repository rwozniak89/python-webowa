import click

@click.command()
@click.option("-a", required=True)
@click.option("-b", required=True)
def dwuparametrowa(a, b):
    print(f'parametr a {a}')
    print(f'parametr b {b}')


dwuparametrowa()