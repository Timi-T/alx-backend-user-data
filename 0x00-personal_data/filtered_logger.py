#!/usr/bin/env python3
"""
Module to obfuscate logs to protect person data
"""


import logging
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function to obfuscate logs"""
    for field in fields:
        pat = field + '=[^{}]*'.format(separator)
        message = re.sub(pat, field + '=' + redaction, message)
    return message


def get_logger() -> logging.Logger:
    """Function to get a logger"""

    user_data = logging.Logger(name='user_data').setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    user_data.addHandler(handler)
    return user_data


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor mmethod for class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format output for logging"""
        formatter = logging.Formatter(self.FORMAT)
        record.msg = filter_datum(list(self.fields), '***', record.msg, ';')
        return formatter.format(record)
