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
    for field in fields:
        pat = field + '=[^{}]*'.format(separator)
        message = re.sub(pat, field + '=' + redaction, message)
    return(message)