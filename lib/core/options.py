#!/usr/bin/env python

from lib.core.init import conf
from lib.core.init import logger


def initOptions(cmdlineargs) -> None:
    """
    Initializes the options by setting the command line arguments to the conf object.
    """
    
    if cmdlineargs.colourless == True:
        from lib.core.log import LOGGER_HANDLER
        from lib.core.log import ColourlessFormatter
        logger.removeHandler(LOGGER_HANDLER)
        LOGGER_HANDLER.setFormatter(ColourlessFormatter())
        logger.addHandler(LOGGER_HANDLER)
    logger.debug("Initializing options...")
    conf.target_url = cmdlineargs.target_url
    conf.cookies = cmdlineargs.cookies
    conf.colourless = cmdlineargs.colourless
    
