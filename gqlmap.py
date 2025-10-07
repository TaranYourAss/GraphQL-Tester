#!/usr/bin/env python

try:
    import sys
    sys.dont_write_bytecode = True

    import cloudscraper
    import json
    import time
    import argparse
    import threading
    import logging
    import traceback
    import plotext as plt

    import lib.parse.cmdargs as cmdargs
    from lib.core.init import conf
    from lib.core.init import logger
    from lib.core.options import initOptions
    from lib.core.settings import BANNER
    from lib.core.common import print_banner
    from lib.core.common import stdoutWrite
    from lib.core.graphql import GraphQL
    from lib.vuln_testing.overload_dos import directive_overloading
    from lib.vuln_testing.overload_dos import alias_overloading


      

except KeyboardInterrupt:
    error = "user aborted during library importing"
    import time
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
# - 
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
        #TODO integrate with GraphQL class
        alias_overloading_data = alias_overloading(url=TARGET.url, headers=TARGET.headers, max_overloads=100000)
        plt.simple_bar(alias_overloading_data[1], alias_overloading_data[0], title="Alias Overloading - Overload Count vs Response Time (ms)", width=100)
        plt.show()
        directive_overloading_data = directive_overloading(url=TARGET.url, headers=TARGET.headers, max_overloads=100000)
        plt.simple_bar(directive_overloading_data[1], directive_overloading_data[0], title="Directive Overloading - Overload Count vs Response Time (ms)", width=100)
        plt.show()
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