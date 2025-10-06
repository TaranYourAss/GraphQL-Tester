#!/usr/bin/env python
import cloudscraper

from lib.core.init import conf
from lib.core.init import logger

def request(url:str, method:str, data=None, json_data=None, headers=None, timeout=10) -> dict:
    """
    Make a request to the specified URL
    
    Args:
        url (str): The URL to send the POST request to
        method (str): HTTP method to use ('GET' or 'POST')
        data (dict, optional): Form data to send (for form-encoded requests)
        json_data (dict, optional): JSON data to send
        headers (dict, optional): Request headers

    """

    try:
        scraper = cloudscraper.create_scraper()
        request_params = {
            'url': url,
            'data': data,
            'json': json_data,
            'headers': headers,
            'timeout': timeout
        }
        if method.lower() == 'get':
            return scraper.get(**request_params)
        elif method.lower() == 'post':
            return scraper.post(**request_params)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        #elapsed_time = response.elapsed.total_seconds()

    
    except cloudscraper.exceptions.CloudflareChallengeError:
        logger.critical("Cloudflare anti-bot protection detected. Unable to bypass.")

    except cloudscraper.exceptions.CloudflareCode1020:
        logger.critical("Cloudflare 1020 Access Denied error encountered.")

    except cloudscraper.exceptions.CloudflareLoopProtection as e:
        logger.critical(f"Cloudflare loop protection detected: {e}")

    except Exception as e:
        logger.critical(f"An error occurred during the request to {request_params['url']}: {e}")