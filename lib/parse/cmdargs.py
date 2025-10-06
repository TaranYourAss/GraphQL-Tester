#!/usr/bin/env python


import argparse


def get_cmd_arguments() -> argparse: 
    parser = argparse.ArgumentParser(description="""GraphQL Mapping & Penetration Testing Tool""")
    parser.add_argument('-u', '--url=', dest='target_url', help='Target URL you want to test.', required=True)
    parser.add_argument('-c', '--cookies=', dest='cookies', help='Cookies for authentication. Example: "session=abc123"', required=False)
    parser.add_argument('--colourless', '--colorless', action='store_true', dest='colourless', help='Use if you want to disable colour in terminal output', required=False)

    args = parser.parse_args()
    return args