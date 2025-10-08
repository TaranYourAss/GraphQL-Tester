#!/usr/bin/env python

try:
    import sys
    sys.dont_write_bytecode = True

    import os
    import requests
    import cloudscraper
    import json
    import time
    import argparse
    import threading
    import logging
    import traceback
    import plotext as plt

    import lib.parse.cmdargs as cmdargs
    from lib.core.init import conf, logger 
    from lib.core.options import initOptions
    from lib.core.settings import BANNER
    from lib.core.common import print_banner, stdoutWrite
    from lib.core.graphql import GraphQL


    conf.term_width = os.get_terminal_size().columns


      
except OSError:
    error = "Could not determine terminal size. Possibly running in a non-terminal environment"

except KeyboardInterrupt:
    error = "User aborted during library importing"

finally:
    if 'error' in locals():
        sys.exit("\r[%s] [CRITICAL] %s" % (time.strftime("%X"), error))

#TODO: 
# - automatically try GET & POST
# - add way to cancel scan while it's running
# - add more format options for queries - not all GraphQL will be JSON in the body
# - add error to let user know if universal queries & introspection aren't enabled
#   - if introspection enabled, check if description fields are available - potentially has sensitive info 
# - test against graphql-armor
# - threading?
# - finish loadingCursor method
# - add option to not verify SSL certificates
# - add option to set timeout
# - add option to set user-agent
# - add way to handle redirects
# - add logging to file option
# - take advantage of rate limiting bypasses
# - make overload tests more robust - handle syntax errors
# - add switch to disabled plotting of overload performance data
# - make features modular so users can pick & choose what to test for
# - display results of test at the end of the scan
#- dynamically set plot width based on terminal size#
#
# - FEATURES
#   - proxy
#   - fingerprint GraphQL engine
#   - attempt through websocket if introspection/universal queries not enabled
#   - attempt CSRF attacks
#   - attempt cross-site websocket hijacking
#   - rate limit bypassing using Aliases 
#   - Alias Overloading
#   - Array-based Query Batching
#   - Field Duplication Vulnerability
#   - Incremental delivery abuse
#   - Field suggestions abuse
#   - GraphQL IDE enable
#   - unhandled errors
#   - Persisted Query Abuse - COPILOT GENEREATED THIS - IDK WHAT THIS IS
#   - Automatic query chaining based on schema - COPILOT GENEREATED THIS - IDK WHAT THIS IS
#   - Authorization Bypass via Introspection - COPILOT GENEREATED THIS - IDK WHAT THIS IS
#   - GraphQL Query Depth Analysis - COPILOT GENEREATED THIS - IDK WHAT THIS IS


def main():
    """
    Main function of gqlmap.
    """
    try:
        args = cmdargs.get_cmd_arguments()
        initOptions(args)

        print_banner(BANNER)

        stdoutWrite(f"[*] Started at %s\n\n" % time.strftime("%X %Y/%m/%d"))


        TARGET = GraphQL()
        TARGET.vuln_scan_all()
        #TODO handle results better - actually tell the user if vulnerable or not


    except requests.exceptions.HTTPError as httpErrMsg:
        logger.critical(f"Error Message: {httpErrMsg}")
        raise SystemExit
    
    except Exception as errMsg:
        excMsg = traceback.format_exc()
        logger.critical("%s\n%s" % (errMsg, excMsg))
        raise SystemExit
    
    finally:
        stdoutWrite("\n[*] Finished at %s\n\n" % time.strftime("%X %Y/%m/%d"))
        

    logger.warning(msg="Test")
    logger.info(msg="Test")
    logger.debug(msg="Test")
    logger.error(msg="Test")
    logger.critical(msg="Test")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        raise
    except:
        traceback.print_exc()
    """
    header={"Content-Type": "application/json"}
    if args.cookies:
        header["Cookie"] = args.cookies
    
    #default to plotting data
    if args.plot_bool and args.plot_bool.lower() in ['false', 'f', '0', 'no', 'n']:
        args.plot_bool = False
    else:
        args.plot_bool = True

    data = directive_overloading(args.target_url, headers=header if args.cookies else None)
    if data and args.plot_bool==True:
        import plotext as plt
        plt.simple_bar(data[1], data[0], title="GraphQL Directive Overloading Performance", width=100)
        plt.show()
    """