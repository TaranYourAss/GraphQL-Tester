#!/usr/bin/env python

COLOURS = {
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'BLACK': '\033[30m',
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'WHITE': '\033[37m',
    'BRIGHT_BLACK': '\033[90m',
    'BRIGHT_RED': '\033[91m',
    'BRIGHT_GREEN': '\033[92m',
    'BRIGHT_YELLOW': '\033[93m',
    'BRIGHT_BLUE': '\033[94m',
    'BRIGHT_MAGENTA': '\033[95m',
    'BRIGHT_CYAN': '\033[96m',
    'BRIGHT_WHITE': '\033[97m',
    'RED_BACKGROUND': '\033[41m',
    'UNDERLINE': '\033[4m'

}


# sqlmap version (<major>.<minor>.<month>.<monthly commit>)
VERSION = "0.3.10.15"
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
    '\\': COLOURS['MAGENTA'],
    '/': COLOURS['MAGENTA'],
    '(': COLOURS['MAGENTA'],
    ')': COLOURS['MAGENTA']
}
#colour associations for the different logging levels
LOGGING_LEVEL_COLOURS = {
    'DEBUG': COLOURS['BRIGHT_CYAN'],
    'INFO': COLOURS['BRIGHT_GREEN'],
    'WARNING': COLOURS['YELLOW'],
    'ERROR': COLOURS['BRIGHT_RED'],
    'CRITICAL': COLOURS['RED_BACKGROUND']
  }

#the maximum amount of time in ms to wait on each overload attack before stopping the test
MAX_RESPONSE_TIME = 60000 #millisecond only

#max amount of items to add to any overload attempt before stopping the test
MAX_OVERLOAD_COUNT = 100000

#default amount of items to add to any quick overload attempt
DEFAULT_QUICK_OVERLOAD_COUNT = 500

#types of overload tests
OVERLOAD_TYPES = ["alias", "directive", "array", "field"]

TECHNIQUES = {
    "overload": {
        "alias": {
            "type": "alias",
            "start_wrapper": "Testing Alias Overloading...",
            "chart_title": "Alias Overloading - Overload Count vs Response Time (ms)",
            "technique_type": "overload",
            "title": "Alias Overloading",
            "technique": "Mitre ATT&CK: T0814 Denial-of-Service",
            "description": "Alias Overloading is an attack that exploits GraphQL's ability to assign unique names (aliases) to fields in a query to request the same data-intensive field hundreds or thousands of times in a single request, overwhelming the server.",
            "severity": "high"
          },
        "directive": {
            "type": "directive",
            "start_wrapper": "Testing Directive Overloading...",
            "chart_title": "Directive Overloading - Overload Count vs Response Time (ms)",
            "technique_type": "overload",
            "title": "Directive Overloading",
            "technique": "Mitre ATT&CK: T0814 Denial-of-Service",
            "description": "Directive Overloading is an attack that exploits GraphQL's @include or @skip directives with complex or recursive conditions to dramatically increase query complexity and exhaust server resources.",
            "severity": "high"
        },
        "array": {
            "type": "array",
            "start_wrapper": "Testing Array-based Query Batching...",
            "chart_title": "Array-based Query Batching - Batch Count vs Response Time (ms)",
            "technique_type": "overload",
            "title": "Array-based Query Batching",
            "technique": "Mitre ATT&CK: T0814 Denial-of-Service",
            "description": "Array-based Query Batching is a technique where multiple queries are sent as a single request in an array to overwhelm server resources and amplify the impact of an attack.",
            "severity": "high"
        },
        "field": {
            "type": "field",
            "start_wrapper": "Testing Field Duplication...",
            "chart_title": "Field Duplication - Field Count vs Response Time (ms)",
            "technique_type": "overload",
            "title": "Field Duplication",
            "technique": "Mitre ATT&CK: T0814 Denial-of-Service",
            "description": "Field Duplication is an attack where an attacker submits a query repeatedly requesting the same field to overwhelm the server's processing resources and potentially cause a denial of service.",
            "severity": "high"
        },
        "circular_query":{
            "type": "circular_query",
            "start_wrapper": "Testing Circular Query via Introspection...",
            "chart_title": "Circular Query - Field Count vs Response Time (ms)",
            "technique_type": "overload",
            "title": "Circular Query",
            "technique": "Mitre ATT&CK: T0814 Denial-of-Service",
            "description": "A Circular Query via Introspection abuses GraphQL's self-documenting nature to discover and craft deeply nested queries that create resource-intensive cycles, potentially leading to a denial of service.",
            "severity": "high"
        }
    },
    "info_leak": {
        "field_suggestions": {
            "type": "field_suggestions",
            "start_wrapper": "Checking if field suggestions are enabled...",
            "technique_type": "info_leak",
            "title": "Field Suggestions",
            "technique": "Mitre ATT&CK: T1592.002 Gather Victim Host Information: Software",
            "description": "Field suggestions are a client-side feature, often powered by GraphQL introspection, that auto-completes available queries and fields, potentially exposing the API schema to anyone accessing the endpoint.",
            "severity": "low"
        }
    }
}
#colour associations for the different severity levels of the techniques
SEVERITY_COLOURS = {
    "info": "BRIGHT_BLUE",
    "low": "BLUE",
    "medium": "YELLOW",
    "high": "RED",
    "critical": "RED_BACKGROUND"
}
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

EXTRA_ENDPOINTS = [
    "/admin"
]

#don't need this at all but its still here
RESULT_TEMPLATE = {
    "Type": "",
    "Title": "",
    "Severity": "",
    "Description": "",
    "Payload": ""
}