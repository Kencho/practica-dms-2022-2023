""" WebQuestion class module.
"""

from typing import Dict, List, Optional
from flask import session
from dms2223common.data.rest import ResponseData
from dms2223frontend.data.rest.backendservice import BackendService
from .webutils import WebUtils


class WebComment():
    """ Monostate class responsible of the user operation utilities.
    """
    @staticmethod
    def list_comments(backend_service:BackendService, id: int) -> Optional[List]:
        """ Gets the list of comments from the backend service.

        Args:
            - backend_service (BackendService): The backend service.

        Returns:
            - List: A list of user data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_comments(session.get('token'), id)
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def create_comment(backend_service: BackendService, discussionid: int, answerid: int, content: str) -> Optional[Dict]:
        """ Creates a comment in the backend service.

        Args:
            - backendservice (BackendService): The backend service.
            - title (str): The title of the discussion to be created.
            - content (str): The content of the discussion to be created.

        Returns:
            - Dict: A dictionary with the newly created user if successful.
            - None: Nothing on error.
        """
        response: ResponseData = backend_service.create_comment(session.get('token'), discussionid, answerid, content)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def get_comment(backend_service: BackendService, id: int) -> Optional[Dict]:
        response: ResponseData = backend_service.get_comment(session.get('token'), id)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def vote_comment(backend_service: BackendService, commentid: int) -> Optional[Dict]:
        response: ResponseData = backend_service.vote_comment(session.get('token'), commentid)
        WebUtils.flash_response_messages(response)
        return response.get_content()