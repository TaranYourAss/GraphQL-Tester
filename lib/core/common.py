#!/usr/bin/env python
import sys

from lib.core.settings import BANNER_CHAR_COLOURS
from lib.core.settings import COLOURS

def stdoutWrite(text: str) -> None:
    """
    Writes text to the stdout (console) stream
    """
    sys.stdout.write(text)

def print_banner(banner:str, coloured_output:bool=True) -> None:
    if coloured_output:
        colored_line = ""
        for char in banner:
            if char == '\n':
                print(colored_line)
                colored_line = ""
            elif char in BANNER_CHAR_COLOURS:
                colored_line += BANNER_CHAR_COLOURS[char] + char + COLOURS.RESET
            else:
                colored_line += char
        if colored_line:
            print(colored_line)
    else:
        print(banner)