#!/usr/bin/env python


import argparse


def get_cmd_arguments() -> argparse: 
    parser = argparse.ArgumentParser(description="""GraphQL Mapping & Penetration Testing Tool""")
    parser.add_argument('-u', '--url=', type=str, dest='target_url', help='Target URL you want to test.', required=True)
    parser.add_argument('-c', '--cookies=', type=str, dest='cookies', help='Cookies for authentication. Example: "session=abc123"', required=False)
    parser.add_argument('--colourless', '--colorless', action='store_true', dest='colourless', help='Use if you want to disable colour in terminal output', required=False)
    parser.add_argument('--max_overload_response=', type=int, dest='max_overload_response', help='Sets the maximum amount of time (seconds) to wait on each overload attack before stopping the test', required=False)
    parser.add_argument('--max_overload_count=', type=int, dest='max_overload_count', help='Sets the maximum amount of directives, aliases, fields, etc to add to any overload attempt before stopping the test', required=False)

    args = parser.parse_args()
    return args