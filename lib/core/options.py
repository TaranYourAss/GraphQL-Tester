#!/usr/bin/env python


from lib.core.init import conf, logger, results


def initOptions(cmdlineargs) -> None:
    """
    Initializes the options by setting the command line arguments to the conf object.
    """
    conf.target_url = cmdlineargs.target_url
    conf.cookies = cmdlineargs.cookies
    conf.colourless = cmdlineargs.colourless
    conf.max_overload_response = cmdlineargs.max_overload_response
    conf.max_overload_count = cmdlineargs.max_overload_count
    conf.full_overload = cmdlineargs.full_overload
    conf.batch = cmdlineargs.batch
    results.vulnerable = []
    results.not_vulnerable = []


    if conf.colourless == True:
        from lib.core.log import LOGGER_HANDLER
        from lib.core.log import ColourlessFormatter
        logger.removeHandler(LOGGER_HANDLER)
        LOGGER_HANDLER.setFormatter(ColourlessFormatter())
        logger.addHandler(LOGGER_HANDLER)
    