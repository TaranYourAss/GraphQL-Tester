#!/usr/bin/env python

import time
import plotext as plt


from lib.utils.http import request
from lib.core.init import logger, conf, results
from lib.core.common import stdoutWrite
from lib.core.settings import MAX_OVERLOAD_COUNT, MAX_RESPONSE_TIME, OVERLOAD_TYPES, DEFAULT_QUICK_OVERLOAD_COUNT
from lib.core.settings import RESULT_TEMPLATE
from lib.core.datatypes import AttribDict

def validateVulnerable(response) -> bool:
    #TODO add better validation of response to make sure the overload worked
    if response and response.status_code == 200:
        return True
    else:
        return False

def init_query(type:str, overload_count:int) -> dict:
    if type == "alias":
        aliases = f" alias{overload_count}: __typename" * overload_count
        json_data = {"query": f"query {type}_test {{{aliases}}}"}

    elif type == "directive":
        json_data = {"query": f"query {type}_test {{__typename {'@include(if:true) ' * overload_count}}}"}

    elif type == "array":
        json_data = []
        for x in range(0, overload_count):
            json_data.append({"query": f"query {type}_test {{__typename}}"})

    elif type == "field":
        fields = f" __typename" * overload_count
        json_data = {"query": f"query {type}_test {{{fields}}}"}

    else:
        logger.error(f"Unknown overload type: {type}")
        #TODO raise exception
        return None
    
    return json_data

def quick_overload(url:str, type:str, headers:str=None, overload_count:int=None) -> list:
    """
    Perform a quick overload test.
    """
    #not used now but could be used in the future
    if overload_count:
        count = overload_count
    else:
        count = DEFAULT_QUICK_OVERLOAD_COUNT

    json_data = init_query(type=type, overload_count=count)

    if json_data is None:
        return None
    
    results = request(
        url=url,
        method='POST',
        json_data=json_data,
        headers=headers,
        timeout=10
    )
    response_time_ms = results.elapsed.total_seconds() * 1000

    #TODO add better validation of response to make sure the overload worked
    return results




def overload(url:str, type, headers:str=None, fullTest:bool=False) -> list:

    performance_data = [[], []] # [response_time_seconds, overload_count]
    overload_count = 1
    while True: #loop until we hit a stopping condition or keyboard interrupt
        try:

            overload_count = overload_count * 2
            if conf.max_overload_count:
                if overload_count > conf.max_overload_count:
                    overload_count = conf.max_overload_count

            elif overload_count > MAX_OVERLOAD_COUNT:
                overload_count = MAX_OVERLOAD_COUNT

            json_data = init_query(type=type, overload_count=overload_count)
            if json_data is None:
                return None
            
            results = request(
                url=url,
                method='POST',
                json_data=json_data,
                headers=headers,
                timeout=240
            )


            #TODO validate response shows alias and alias1 for alias overloading
            #TODO handle syntax errors
            # - Unknown directive 
            # - The directive "@include" may only be used once

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


            
            if response_time_ms >= MAX_RESPONSE_TIME: #if the response time is over 60 seconds stop the test
                logger.info(f"Response time exceeded maximum default time of {MAX_RESPONSE_TIME / 1000} seconds, stopping test")
                break
            
            elif overload_count >= MAX_OVERLOAD_COUNT:
                logger.info(f"Reached default maximum overload count of {MAX_OVERLOAD_COUNT}, stopping test")
                break

            
            if conf.max_overload_response:
                # we assume the user set a value in seconds so convert to ms
                if response_time_ms >= conf.max_overload_response * 1000:
                    logger.info(f"Response time exceeded user set maximum time of {conf.max_overload_response} seconds, stopping test")
                    break

            elif conf.max_overload_count:
                if overload_count >= conf.max_overload_count:
                    logger.info(f"Reached user set maximum overload count of {conf.max_overload_count}, stopping test")
                    break
            
            # TODO: add a way to check if the response time is constnantly increasing
            # need to make sure that the repsonse times are tied to the overload count
            # - if the overload count is increasing but the response time is not the application is not vulnerable
            #    - could be using timouts to kill processing of the query
            #    - could have a limit to directives
            #    - could be filtering directives with a WAF
            #x += 1
            time.sleep(0.5) #be nice to the server
        except KeyboardInterrupt:
            logger.info("Keyboard interrupt received, stopping test")
            break
    return performance_data

def overload_all(url:str, headers:str=None) -> None:
    #TODO add way to turn off plotting data
    """
    Perform all overload tests and return the performance data.
    """
    overload_types = OVERLOAD_TYPES

    for overload_type in overload_types:
        OVERLOADTEST = AttribDict()

        if overload_type == 'alias':
            logger.info("Testing Alias Overloading...")
            OVERLOADTEST.chart_title = f"{overload_type.capitalize()} Overloading - Overload Count vs Response Time (ms)"
            OVERLOADTEST.type = "Alias Overloading"            

        elif overload_type == 'directive':
            logger.info("Testing Directive Overloading...")
            OVERLOADTEST.chart_title = f"{overload_type.capitalize()} Overloading - Overload Count vs Response Time (ms)"
            OVERLOADTEST.type = "Directive Overloading"

        elif overload_type == 'array':
            logger.info("Testing Array-based Query Batching...")
            OVERLOADTEST.chart_title = f"Array-based Query Batching - Batch Count vs Response Time (ms)"
            OVERLOADTEST.type = "Array-based Query Batching"

        elif overload_type == 'field':
            logger.info("Testing Field Duplication...")
            OVERLOADTEST.chart_title = f"Field Duplication - Field Count vs Response Time (ms)"
            OVERLOADTEST.type = "Field Duplication"
        
        else:
            logger.error(f"Unknown overload type: {overload_type}")
            continue
        
        OVERLOADTEST.payload = init_query(type=overload_type, overload_count=5)
        print(type(OVERLOADTEST.payload))
        print(OVERLOADTEST.payload)
        exit()


        if conf.full_overload:
            performance_data = overload(url=url, type=overload_type, headers=headers, fullTest=True)
            if performance_data is None:
                continue

            # Determine plot width based on terminal size
            if conf.term_width > 100:
                width = 100
            else:
                width = conf.term_width

            #TODO tell user if vulnerable or not
            
            plt.simple_bar(performance_data[1], performance_data[0], title=OVERLOADTEST.chart_title, width=width)
            plt.show()
            stdoutWrite("\n")
        else:
            response = quick_overload(url=url, type=overload_type, headers=headers)

            if response is None:
                logger.error(f"Skipping {overload_type} test due to error in generating query.")
                continue

            result = RESULT_TEMPLATE.copy()
            result["Type"] = "Overload"
            result["Title"] = OVERLOADTEST.type
            result["Payload"] = OVERLOADTEST.payload['query']

            if validateVulnerable(response):
                results.vulnerable.append(result)
            else:
                results.not_vulnerable.append(result)