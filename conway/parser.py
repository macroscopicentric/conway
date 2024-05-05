import json

"""
Accepts a file in some specific formats (currently json or txt) and
returns an array of arrays of 1s and 0s that can be turned into a Grid.

There's probably a lot more sanity checking I can add in here to protect myself (ex: are all rows/columns the same length, better whitespace protection in txt files)
but I'm not going to worry about that for now.
"""


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        if len(file_path.split(".")) > 1:
            self.file_format = file_path.split(".")[-1]
        else:
            self.file_format = ""

    def parse(self):
        match self.file_format:
            case "json":
                return self.parse_json()
            case "txt":
                return self.parse_txt()
            case _:
                try:
                    print(
                        f"Initial grid file missing extension. Attempting to parse as text file."
                    )
                    return self.parse_txt()
                except:
                    print(
                        f"Oops! I don't know how to parse this file. Please add a valid extension from [json, txt] matching one of the examples in the examples directory and try again."
                    )
                    raise

    def parse_json(self):
        with open(self.file_path) as f:
            return json.load(f)

    def parse_txt(self):
        with open(self.file_path) as f:
            return [[int(char) for char in list(line.strip())] for line in f]
