#!usr/bin/env python3
"""
Module to obfuscate logs to protect person data
"""


import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function to obfuscate logs"""
    for field in fields:
        pat = field + '=[^{}]*'.format(separator)
        message = re.sub(pat, field + '=' + redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor mmethod for class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
