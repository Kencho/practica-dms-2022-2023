""" WebQuestion class module.
"""

from typing import Dict, List, Optional
from flask import session
from dms2223common.data.rest import ResponseData
from dms2223frontend.data.rest.backendservice import BackendService
from .webutils import WebUtils


class WebAnswer():
    """ Monostate class responsible of the user operation utilities.
    """
    @staticmethod
    def list_answers(backend_service:BackendService, id: int) -> Optional[List]:
        """ Gets the list of discussions from the backend service.

        Args:
            - backend_service (BackendService): The backend service.

        Returns:
            - List: A list of user data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_answers(session.get('token'), id)
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def create_answer(backend_service: BackendService, discussionid: int, content: str) -> Optional[Dict]:
        """ Creates a discussion in the backend service.

        Args:
            - backendservice (BackendService): The backend service.
            - title (str): The title of the discussion to be created.
            - content (str): The content of the discussion to be created.

        Returns:
            - Dict: A dictionary with the newly created user if successful.
            - None: Nothing on error.
        """
        response: ResponseData = backend_service.create_answer(session.get('token'), discussionid, content)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def get_answer(backend_service: BackendService, answerid: int) -> Optional[Dict]:
        response: ResponseData = backend_service.get_answer(session.get('token'), answerid)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    
    @staticmethod
    def vote_answer(backend_service: BackendService, answerid: int) -> Optional[Dict]:
        response: ResponseData = backend_service.vote_answer(session.get('token'), answerid)
        WebUtils.flash_response_messages(response)
        return response.get_content()