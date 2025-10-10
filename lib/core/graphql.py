#!/usr/bin/env python

from lib.core.init import conf, logger
from lib.core.common import handleExit
from lib.utils.http import request

from lib.vuln_testing.overload_dos import overload_all


class GraphQL:
    def __init__(self) -> None:
        self.url = conf.target_url
        self.headers = {
            'Content-Type': 'application/json'
        }
        if conf.cookies:
            self.headers['Cookie'] = conf.cookies

        logger.info(f"Testing connection to the target URL: {self.url}...")
        self.test_connection()
            

        logger.info(f"OK")

    def send_query(self, query:str) -> dict:
        payload = {
            'query': query
        }
        response = request(
            url=self.url,
            method='POST',
            json_data=payload,
            headers=self.headers,
            timeout=10
        )
        return response

    def test_connection(self) -> bool:
        try:
            response = request(
                url=self.url,
                method='POST',
                headers=self.headers,
                json_data={"query": "{ __typename }"},
                timeout=10
            )
            if response and response.status_code == 200:
                return True
            elif response and response.status_code == 400:
                logger.warning(f"Connected to {self.url}, but received a 400 Bad Request. This indicates that the endpoint is reachable but the default GrapQL test query ('query': '{{ __typename }}') may be malformed.")
                return True
            else:
                logger.error(f"Failed to connect to {self.url}. Status code: {response.status_code if response.status_code else 'No Response'}")
                return False
        except Exception as e:
            logger.error(f"An error occurred while trying to connect to {self.url}: {e}")
            handleExit("Unable to connect to the target URL", 1)
        
    def vuln_scan_all(self) -> None:
        #TODO add ability to select level of testing
        overload_all(url=self.url, headers=self.headers)
        #TODO add other vuln tests here