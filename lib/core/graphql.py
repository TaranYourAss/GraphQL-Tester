#!/usr/bin/env python

from lib.core.init import conf
from lib.core.init import logger
from lib.utils.http import request

class GraphQL:
    def __init__(self) -> None:
        self.url = conf.target_url
        self.headers = {
            'Content-Type': 'application/json'
        }
        if conf.cookies:
            self.headers['Cookie'] = conf.cookies

        logger.info(f"Attempting to connect to: {self.url}...")

        if self.test_connection() == False:
            logger.critical("Unable to connect to the target URL.")
        logger.info(f"\rOK")

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
                logger.warning(f"Connected to {self.url}, but received a 400 Bad Request. This indicates that the endpoint is valid but the default GrapQL test query ('query': '{{ __typename }}') is malformed.")
                return True
            else:
                logger.error(f"Failed to connect to {self.url}. Status code: {response.status_code if response.status_code else 'No Response'}")
                return False
        except Exception as e:
            logger.error(f"An error occurred while trying to connect to {self.url}: {e}")
            return False