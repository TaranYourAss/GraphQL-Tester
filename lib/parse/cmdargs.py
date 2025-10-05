#!/usr/bin/env python


import argparse


def get_cmd_arguments() -> argparse: 
    parser = argparse.ArgumentParser(description="""GraphQL Directive Overloading Tester""")
    parser.add_argument('-u', '--url', dest='target_url', help='Target URL you want to test.', required=True)
    parser.add_argument('-c', '--cookies', dest='cookies', help='Cookies for authentication. Example: "session=abc123"', required=False)
    args = parser.parse_args()
    return args