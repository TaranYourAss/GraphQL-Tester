#!/usr/bin/env python

import logging
import sys
import re

from lib.core.common import COLOURS
from lib.core.settings import LOGGING_LEVEL_COLOURS as level_colours
LOGGER = logging.getLogger("gqlmapLog")

class ColouredFormatter(logging.Formatter):
    def __init__(self):
        super().__init__("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
    
    def format(self, record):
        result = super().format(record)
        
        level_colour = level_colours.get(record.levelname, COLOURS.RESET)
        result = result.replace(
            f"[{record.levelname}]", 
            f"[{level_colour}{record.levelname}{COLOURS.RESET}]"
        )
        
        # Color the timestamp (first [HH:MM:SS] pattern)
        result = re.sub(
            r'\[(\d{2}:\d{2}:\d{2})\]', 
            f'[{COLOURS.MAGENTA}\\1{COLOURS.RESET}]', 
            result, 
            count=1
        )
        
        return result


#LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = ColouredFormatter()

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.INFO)
