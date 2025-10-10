#!/usr/bin/env python
import sys

from lib.core.settings import BANNER_CHAR_COLOURS, COLOURS, SEVERITY_COLOURS
from lib.core.init import conf, logger, results



def addColour(text:str, colour:str) -> str:
    """
    Adds ANSI colour codes to the given text.
    """
    if conf.colourless:
        return text
    else:
        return f"{COLOURS[f'{colour.upper()}']}{text}{COLOURS['RESET']}"

def stdoutWrite(text: str) -> None:
    """
    Writes text to the stdout (console) stream
    """
    sys.stdout.write(text)

def handleExit(msg:str=None, code:int=None) -> None:
    """
    Handles exiting the program with an optional message and exit code.
    """
    if msg and code == 0:
        logger.info(msg)
    elif msg and code != 0:
        logger.critical(msg)
    
    if code != 0:
        logger.critical("Exiting...")
    else:
        logger.info("Exiting...")
    sys.exit(code if code else 0)

def print_banner(banner:str) -> None:
    if conf.colourless == False:
        colored_line = ""
        for char in banner:
            if char == '\n':
                print(colored_line)
                colored_line = ""
            elif char in BANNER_CHAR_COLOURS:
                colored_line += BANNER_CHAR_COLOURS[char] + char + COLOURS['RESET']
            else:
                colored_line += char
        if colored_line:
            print(colored_line)
    else:
        print(banner)

def ask_yes_or_no(question:str) -> bool:
    """
    Recieve input from user. Only accepts y or n. 

    Returns True if y / False if n
    """
    answered = False
    while answered == False:
        ask = str(input(question))
        if ask.lower() == "y" or ask == "":
            return True
        elif ask.lower() == "n":
            return False
        else:
            stdoutWrite("\nInvalid input. Please enter 'y', 'n', or press Enter for 'y'.")

def displayResults() -> None:
    if results.vulnerable:
        stdoutWrite("\ngqlmap identified the target to be vulnerable to the following:")
        stdoutWrite("\n---")
        stdoutWrite(f"\n{addColour("Vulnerable:", "BRIGHT_RED")}")
        for vuln in results.vulnerable:
            stdoutWrite(f"\n    Type: {vuln['Type']} - {vuln['Technique']}")
            stdoutWrite(f"\n    Title: {vuln['Title']}")
            if vuln['Severity'] in SEVERITY_COLOURS:
                severity = addColour(vuln['Severity'], SEVERITY_COLOURS[vuln['Severity']])
            else:
                severity = vuln['Severity']
            stdoutWrite(f"\n    Severity: {severity}")
            stdoutWrite(f"\n    Description: {vuln['Description']}")
            stdoutWrite(f"\n    Payload: {vuln['Payload']}")
            stdoutWrite("\n")
            

    if results.not_vulnerable:
        stdoutWrite("\ngqlmap attempted the following but found the target to not be vulnerable:")
        stdoutWrite("\n---")
        stdoutWrite(f"\n{addColour("Not Vulnerable:", "BRIGHT_GREEN")}")
        for vuln in results.not_vulnerable:
            stdoutWrite(f"\n    Type: {vuln['Type']} - {vuln['Technique']}")
            stdoutWrite(f"\n    Title: {vuln['Title']}")
            if vuln['Severity'] in SEVERITY_COLOURS:
                severity = addColour(vuln['Severity'], SEVERITY_COLOURS[vuln['Severity']])
            else:
                severity = vuln['Severity']
            stdoutWrite(f"\n    Severity: {severity}")
            stdoutWrite(f"\n    Description: {vuln['Description']}")
            stdoutWrite(f"\n    Payload: {vuln['Payload']}")
            stdoutWrite("\n")
    stdoutWrite("\n---")