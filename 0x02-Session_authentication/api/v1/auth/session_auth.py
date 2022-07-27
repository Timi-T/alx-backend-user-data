#!/usr/bin/env python3
"""Session authentication module"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Class to authenticate a session"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session id for a user"""
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = uuid.uuid4()
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
