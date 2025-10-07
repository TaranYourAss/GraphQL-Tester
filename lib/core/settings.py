#!/usr/bin/env python

class COLOURS:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    RED_BACKGROUND = '\033[41m'

# sqlmap version (<major>.<minor>.<month>.<monthly commit>)
VERSION = "0.2.10.7"
DESCRIPTION = "GraphQL mapping + vulnerability scanner"

BANNER_OLD = rf"""
                   ███                   
                 ███████                 
                ███▓║▓███                
               ███████████               
            ████ ███████ ████            
  ████   ████   ██▒  ▒ ██   ████   ████  
█████████      ██▒▒   ▒ ██      █████████
██▓║║▓██      ██▒      ▒▒██      ██▓║║▓██
████████     ██ ▒▒    ▒▒  ██     ████████
   ███      ██▒   ▒   ▒  ▒▒██      ███   
   ██      ██  ▒   ███   ▒  ██      ██   
   ██     ██▒  ▒▒ █████ ▒   ▒██     ██   
   ██   ███▒    ▒███ ███  ▒▒▒ ███   ██   
   ██  ███▒ ▒▒▒▒ ███████ ▒    ▒███  ██   
   ██ ███▒      ▒▒  ▒  ▒▒    ▒▒ ███ ██   
   ████▒▒   ▒  ▒▒   ▒▒   ▒▒  ▒   ▒████   
 ███████ ▒▒▒ ▒▒   ▒▒  ▒   ▒▒▒  ▒▒███████ 
██▓║║▓█████████████████████████████▓║║▓██
█████████                       █████████
  ████   ████               ████   ████  
            ████   ███   ████            
               ███████████               
                ███▓║▓███                
                 ███████                 
                   ███             gqlmap

"""
BANNER = rf"""
                  ░████                                                                         
                ░████████                                                                       
                ░███░░███                                                                       
               ░██████████                                                                      
            ░███  ██████ ░███                                                                   
  ░████ ░████   ░██    ██   ░████ ░████                                                         
░█████████     ░██      ██     ░█████████                                                       
░███░░███     ░██   /\   ██     ░███░░███                                                       
░████████   ░███   /  \   ███   ░████████                                                       
  ░████    ░███   /    \   ███    ░████                                                         
   ░██    ░███   / █▄▄█ \   ███    ░██      ░██████  ░██████ ░██     ░███   ░███ ░█████ ░██████ 
   ░██   ░███   (▄██  ██▄)   ███   ░██     ░██      ░██   ░██░██ /▄\ ░████ ░████░██  ░██░██  ░██
   ░██  ░██     (▀██  ██▀)     ██  ░██     ░██  ░███░██   ░██░██ \▀/ ░██░████░██░███████░██████ 
   ░██ ░██       \ █▀▀█ /       ██ ░██     ░██   ░██░██ ▄▄░██░██     ░██ ░██ ░██░██  ░██░██     
   ░██░██         \    /         ██░██      ░██████  ░██████ ░███████░██     ░██░██  ░██░██     
  ░█████           \  /           █████                  ▀▀                                     
░████████           \/           ████████                    -v{VERSION}-                       
░███░░██████████████████████████████░░███                                                       
░█████████                     ░█████████                                                       
 ░░████ ░████               ░███  ░████                                                         
            ░███  ░████  ░███                                                                   
               ░██████████                                                                      
                ░███░░███                                                                       
                ░████████                                                                       
                  ░████                                                                         
                  """
#colours associations for the banner characters
BANNER_CHAR_COLOURS = {
    '\\': COLOURS.MAGENTA,
    '/': COLOURS.MAGENTA,
    '(': COLOURS.MAGENTA,
    ')': COLOURS.MAGENTA
}
#colour associations for the different logging levels
LOGGING_LEVEL_COLOURS = {
    'DEBUG': COLOURS.BRIGHT_CYAN,
    'INFO': COLOURS.BRIGHT_GREEN,
    'WARNING': COLOURS.YELLOW,
    'ERROR': COLOURS.BRIGHT_RED,
    'CRITICAL': COLOURS.RED_BACKGROUND
  }

#the maximum amount of time in ms to wait on each overload attack before stopping the test
MAX_RESPONSE_TIME = 60000 #millisecond only

#max amount of directives to add to any overload attempt before stopping the test
MAX_OVERLOAD_COUNT = 100000

OVERLOAD_TYPES = ["alias", "directive", "array", "field"]

#Common GraphQL endpoints
GRAPHQL_ENDPOINTS = [
    "/graphql",
    "/graphiql",
    "/api/graphql",
    "/api/graphiql",
    "/v1/graphql",
    "/v1/graphiql",
    "/api/v1/graphql",
    "/api/v1/graphiql",
    "/gql",
    "/gql/v1",
    "/gql/v2"
]