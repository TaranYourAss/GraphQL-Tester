#!/usr/bin/env python

from lib.core.init import conf
from lib.core.log import logger
from lib.utils.http import request

class GraphQL:
    def __init__(self) -> None:
        self.url = conf.target_url
        self.headers = {
            'Content-Type': 'application/json'
        }
        if conf.cookies:
            self.headers['Cookie'] = conf.cookies

        if self.test_connection(self) == False:
            logger.critical("Unable to connect to the target URL.")

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
                timeout=10
            )
            if response and response.status_code == 200:
                return True
            else:
                logger.error(f"Failed to connect to {self.url}. Status code: {response.status_code if response else 'No Response'}")
                return False
        except Exception as e:
            logger.error(f"An error occurred while trying to connect to {self.url}: {e}")
            return False