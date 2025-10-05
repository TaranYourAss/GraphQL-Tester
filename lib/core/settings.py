#!/usr/bin/env python

class COLOURS:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

# sqlmap version (<major>.<minor>.<month>.<monthly commit>)
VERSION = "0.1.10.5"
DESCRIPTION = "GraphQL mapping + vulnerability scanner"

BANNER = f"""

                    ███                    
                  ███████                  
                 ███▓|▓███                 
                ███████████                
   ▀▀▀▀      ████ ███████ ████      ▀▀▀▀   
   ████   ████   ██▒▒ ▒ ██   ████   ████   
▌█████████      ██▒▒   ▒ ██      █████████▐
▌██▓▐▌▓██      ██▒   ▒  ▒▒██      ██▓▐▌▓██▐
▌████████     ██ ▒▒ ▒  ▒▒  ██     ████████▐
    ███      ██▒   ▒ ▒ ▒  ▒▒██      ███    
   ▌██      ██  ▒   ███   ▒  ██      ██▐   
   ▌██     ██▒  ▒▒ █░║░█ ▒   ▒██     ██▐   
   ▌██   ███▒▒   ▒██░║░██  ▒▒▒ ███   ██▐   
   ▌██  ███▒  ▒▒▒ ███████ ▒    ▒███  ██▐   
   ▌██ ███       ▒▒  ▒  ▒▒    ▒▒ ███ ██▐   
    ████▒▒   ▒  ▒▒   ▒▒   ▒▒  ▒   ▒████    
  ███████ ▒▒▒ ▒▒    ▒  ▒   ▒▒▒   ▒███████  
▌██▓▐▌▓█████████████████████████████▓▐▌▓██▐
▌█████████                       █████████▐
   ████   ████               ████   ████   
   ▄▄▄▄      ████   ███   ████      ▄▄▄▄   
                ███████████                
                 ███▓|▓███                 
                  ███████                  
                    ███              gqlmap
"""
#colours associations for the banner characters
BANNER_CHAR_COLOURS = {
    '║': COLOURS.BRIGHT_RED,
    '|': COLOURS.BRIGHT_WHITE,
    '▒': COLOURS.BRIGHT_MAGENTA,
    '░': COLOURS.BRIGHT_WHITE,   
    '▓': COLOURS.BRIGHT_BLUE,    
    '█': COLOURS.BRIGHT_BLACK   
}


#the maximum amount of time in ms to wait on each directive overload attack before stopping the test
DIRECTIVE_OVERLOAD_MAX_RESPONSE_TIME = 60000

#max amount of directives to add to any directive overload attempt
DIRECTIVE_OVERLOAD_MAX_DIRECTIVE_COUNT = 100000