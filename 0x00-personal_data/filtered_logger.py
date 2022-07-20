#!usr/bin/env python3
"""
Module to obfuscate logs to protect person data
"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function to obfuscate logs

    fields: A list of fields in the log to be replaced
    redaction: String to replace field
    message: A line of log
    separator: String that separate each field

    The function returns a new string with replaced fields if any.
    """
    new = message
    for i in range(len(fields)):
        pat = ((new.split(fields[i] + '='))[1].split(separator))[0]
        new = re.sub(fields[i] + '=' + pat, fields[i] + '=' + redaction, new)
    return(new)
