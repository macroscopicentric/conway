"""
A lil helper class to manage the hacky ANSI escape sequence shenanigans
I'm doing to manage the little animation that happens when you run this
with terminal output.

I enthusiastically filched most of this from Stack Overflow: https://stackoverflow.com/questions/66615552/display-multi-line-python-console-ascii-animation
"""


class Renderer:
    def __init__(self, number_of_lines):
        self.number_of_lines = number_of_lines

    # Remember the number of lines and original cursor position
    # so we can go back after every print.
    def prep_terminal(self):
        # scroll up to make room for output
        print(f"\033[{self.number_of_lines}S", end="")
        # move cursor back up
        print(f"\033[{self.number_of_lines}A", end="")
        # save current cursor position
        print("\033[s", end="")

    # Go back to the saved cursor position before printing [the
    # newest version of the grid]
    def render(self, obj):
        print("\033[u", end="")
        print(obj)
