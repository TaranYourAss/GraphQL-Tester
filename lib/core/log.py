#!/usr/bin/env python

import logging
import sys


LOGGER = logging.getLogger("gqlmapLog")


#LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.INFO)
