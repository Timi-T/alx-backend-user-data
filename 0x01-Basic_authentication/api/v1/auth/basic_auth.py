#!/usr/bin/env python3
"""
Basic Authentication module
"""

from typing import Tuple
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic authentication class"""

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """Extract base 64 part of Authorization header"""
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        check_basic = authorization_header.split(' ')
        if (check_basic)[0] != 'Basic':
            return None
        return check_basic[1]

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header: str
                                            ) -> str:
        """Decode Base 64 string"""
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
                                    self,
                                    decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Extract user credentials"""
        if not decoded_base64_authorization_header:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        credentials = decoded_base64_authorization_header.split(':')
        if len(credentials) == 1:
            return (None, None)
        return (credentials[0], credentials[1])
