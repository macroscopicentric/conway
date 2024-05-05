import argparse
import sys
import time

from conway.grid import Grid
from conway.parser import Parser
from conway.renderer import Renderer


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-f",
        help="the location of the json-formatted starter file",
        type=str,
        default="examples/blinker.json",
    )
    args = arg_parser.parse_args()

    parser = Parser(args.f)
    grid = Grid(parser.parse())

    renderer = Renderer(grid.column_length)
    renderer.prep_terminal()
    while True:
        renderer.render(grid)
        grid.transition()
        time.sleep(1)


if __name__ == "__main__":
    main()
