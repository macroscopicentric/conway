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

## Wishlist

Things I think would be fun:
- [x] passing in a json file of a starting config
- [ ] refactoring in separate responsibilities and adding some tests
- [ ] adding in new types of organisms and interactions
- [ ] a separate front end that allows some interactivity