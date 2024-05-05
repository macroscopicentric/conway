# Conway

A simple version of Conway's Game of Life.

## Installation

This project depends on [poetry](https://python-poetry.org/). Once you have poetry installed, install Conway's dependencies:

```sh
poetry install
```

## Usage

You can start the script via:
```sh
poetry run main [-f file_path_to_initial_grid]
```

where `file_path_to_initial_grid` is a JSON file that includes an initial grid display to start the transitions from. By default as an example, the script will use `blinker.json` included in the `examples` directory in this module.

## Development

This code base doesn't currently have any tests but it is formatted with black, which you can run with:

```sh
poetry run black .
```

## Wishlist

Things I think would be fun:
- [x] passing in a json file of a starting config
- [x] json got tedious real fast. allow import via simple text files
- [ ] refactoring in separate responsibilities and adding some tests
- [ ] adding in new types of organisms and interactions
- [ ] i think i'm misusing exception handling in the parser, fix that
- [ ] a separate front end that allows some interactivity (clicking to spawn new live cells?!)