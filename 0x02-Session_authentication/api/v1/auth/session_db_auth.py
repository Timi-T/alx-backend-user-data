#!/usr/bin/env python3
"""
Stores a session for user
"""

from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Class to store a session for a user"""

    def create_session(self, user_id=None):
        """Create and stores a data for each session"""
        return super().create_session(user_id)

    def user_id_for_session_id(self, session_id=None):
        """Get a user id from database using session id"""
        return super().user_id_for_session_id(session_id)

    def destroy_session(self, request=None):
        """Destroy a user session"""
        super().destroy_session(request)
