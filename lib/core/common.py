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
        #issue where the first line is messed up
        lines = banner.strip().split('\n')
        for line in lines:
            colored_line = ""
            for char in line:
                if char in BANNER_CHAR_COLOURS:
                    colored_line += BANNER_CHAR_COLOURS[char] + char + COLOURS.RESET
                else:
                    colored_line += char
            print(colored_line)
    else:
        print(banner)