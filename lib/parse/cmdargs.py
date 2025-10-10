#!/usr/bin/env python


import argparse


def get_cmd_arguments() -> argparse: 
    parser = argparse.ArgumentParser(description="""GraphQL Mapping & Penetration Testing Tool""")
    parser.add_argument('-u', '--url=', type=str, dest='target_url', help='Target URL you want to test.', required=True)
    parser.add_argument('-c', '--cookies=', type=str, dest='cookies', help='Cookies for authentication. Example: "session=abc123"', required=False)
    parser.add_argument('--colourless', '--colorless', action='store_true', dest='colourless', help='Use if you want to disable colour in terminal output', required=False)
    parser.add_argument('--max_overload_response=', type=int, dest='max_overload_response', help='Sets the maximum amount of time (seconds) to wait on each overload attack before stopping the test', required=False)
    parser.add_argument('--max_overload_count=', type=int, dest='max_overload_count', help='Sets the maximum amount of directives, aliases, fields, etc to add to any overload attempt before stopping the test', required=False)
    parser.add_argument('--full_overload', action='store_true', dest='full_overload', help='Use if you want to test if denial-of-service is possible (skips being asked if you want to confirm if dos is possible for every overload attempt)', required=False)
    parser.add_argument('--batch', action='store_true', dest='batch', help='Use if you want to skip asking user input - uses default behaviour', required=False)
    parser.add_argument('--quick_overload', action='store_true', dest='quick_overload', help='Use if you do not want to test if denial-of-service is possible on overloads (skips being asked if you want to confirm if dos is possible for every overload attempt)', required=False)

    args = parser.parse_args()
    return args