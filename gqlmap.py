#!/usr/bin/env python
__version__ = "1.0.0"

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

    import lib.parse.cmdargs as cmdargs
    from lib.core.init import conf
    from lib.core.init import logger
    from lib.core.options import initOptions
    from lib.core.settings import BANNER
    from lib.core.common import print_banner
    from lib.core.common import stdoutWrite
    from lib.core.graphql import GraphQL


      

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
# - finish loading cursor
# - add option to not verify SSL certificates
# - add option to set timeout
# - add option to set user-agent
# - 
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

"""
def directive_overloading(url, headers=None):
    
    Returns performance data which contains two lists: [response_time_milliseconds, overload_count]
    
    query = "query overload {__typename @include(if:true) @include(if:true) @include(if:true)}"
    performance_data = [[], []] # [response_time_milliseconds, overload_count]
    #response_tracking = []
    
    #make sure it is a valid url and works
    results = make_post_request(
        url=url,
        json_data={"query": query},
        headers=headers
    )

    #TODO: add something to detect if cloudflare is blocking us
    # Cloudflare</title>
    # <h1 data-translate="block_headline">Sorry, you have been blocked</h1>
    # 
    print(f"Initial test of {url}")
    print(f"Status Code: {results['status_code']}, Response Time (ms): {results['response_time_milliseconds']}, Query: {query}")
    
    if results['status_code'] == 403:
        print(results['content'])
        exit()

    if results['json'] is None:
        print("Response is not JSON, something went wrong")
        print(results['content'])
        return
    #might need to get rid of this to handle other GraphQL engines
    if 'data' not in results['json']:
        print("No data field in response, something went wrong")
        print(results['content'])
        return
    
    #baseline_response_time = results['response_time_milliseconds']
    #x = 0
    overload_count = 3
    while True: #loop until we hit a stopping condition
        overload_count = overload_count * 2
        query = f"query overload {{__typename {'@include(if:true) ' * overload_count}}}"
        results = make_post_request(
            url=url,
            json_data={"query": query},
            headers=headers
        )
        if results['status_code'] == 403:
            print(results['content'])
            exit()
        #if not 'data' in results['json']:
        #    print("No data field in response, something went wrong")
        #    print(results['content'])
        #    return
        #check if we got a non-200 status code, cloudflare may timeout or block us
        if results['status_code'] != 200:
            print(f"Non-200 status code received, stopping test. Status Code: {results['status_code']} - Response Time (ms): {results['response_time_milliseconds']}")
            if "y" or "yes" in input("Do you want to see the full response? (y/n): ").lower():
                print(results['content'])
            return performance_data
        
        performance_data[1].append(overload_count)
        performance_data[0].append(results['response_time_milliseconds'])
        

        print(f"Overload Count: {overload_count} - Response Time (ms): {results['response_time_milliseconds']}")

        if results['response_time_milliseconds'] > 60000: #if the response time is over 60 seconds stop the test
            print("Response time exceeded 60 seconds, stopping test")
            break
        
        # TODO: add a way to check if the response time is constnantly increasing
        # need to make sure that the repsonse times are tied to the overload count
        # - if the overload count is increasing but the response time is not the application is not vulnerable
        #    - could be using timouts to kill processing of the query
        #    - could have a limit to directives
        #    - could be filtering directives with a WAF
        #x += 1
        time.sleep(1) #be nice to the server
    return performance_data
    """
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

    except Exception as errMsg:
        excMsg = traceback.format_exc()
        logger.critical("%s\n%s" % (errMsg, excMsg))
        raise SystemExit
        

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