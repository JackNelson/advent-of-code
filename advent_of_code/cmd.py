import importlib
import click

@click.command()
@click.option("-y", "--year", required=True, help="advent of code year")
@click.option("-d", "--day", required=True, help="advent of code day")
@click.option("-p", "--part", required=False, show_default=True, default=None, help="advent of code part")
@click.option("--test", is_flag=True, show_default=True, default=False, help="whether to use test data")
def main(year: int, day: int, part: int, test: bool = False):

    aoc_module = importlib.import_module(f"advent_of_code.y{year}.d{day}")
    aoc_module.main(test=test, part=part)
