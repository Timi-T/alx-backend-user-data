#!/usr/bin/env python3
"""
Basic Authentication module
"""

from api.v1.auth.auth import Auth


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
