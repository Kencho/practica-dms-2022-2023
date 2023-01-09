""" WebQuestion class module.
"""

from typing import Dict, List, Optional
from flask import session
from dms2223common.data.rest import ResponseData
from dms2223frontend.data.rest.backendservice import BackendService
from .webutils import WebUtils


class WebQuestion():
    """ Monostate class responsible of the user operation utilities.
    """
    @staticmethod
    def list_discussions(backend_service:BackendService) -> List:
        """ Gets the list of discussions from the backend service.

        Args:
            - backend_service (BackendService): The backend service.

        Returns:
            - List: A list of user data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_discussions(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def create_report(backend_service: BackendService,id :Optional[str],reason: Optional[str])-> Optional[Dict]:
        """ Creates a discussion in the backend service.

        Args:
            - backendservice (BackendService): The backend service.
            - title (str): The title of the discussion to be created.
            - content (str): The content of the discussion to be created.

        Returns:
            - Dict: A dictionary with the newly created user if successful.
            - None: Nothing on error.
        """
        response: ResponseData = backend_service.create_report(session.get('token'),id=id,reason=reason)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def create_reportcomment(backend_service: BackendService,id :Optional[str],reason: Optional[str])-> Optional[Dict]:
        """ Creates a discussion in the backend service.

        Args:
            - backendservice (BackendService): The backend service.
            - title (str): The title of the discussion to be created.
            - content (str): The content of the discussion to be created.

        Returns:
            - Dict: A dictionary with the newly created user if successful.
            - None: Nothing on error.
        """
        response: ResponseData = backend_service.create_report_comment(session.get('token'),id=id,reason=reason)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def create_reportanswer(backend_service: BackendService,id :Optional[str],reason: Optional[str])-> Optional[Dict]:
        """ Creates a discussion in the backend service.

        Args:
            - backendservice (BackendService): The backend service.
            - title (str): The title of the discussion to be created.
            - content (str): The content of the discussion to be created.

        Returns:
            - Dict: A dictionary with the newly created user if successful.
            - None: Nothing on error.
        """
        response: ResponseData = backend_service.create_report_answer(session.get('token'),id=id,reason=reason)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def create_discussion(backend_service: BackendService, title: str, content: str) -> Optional[Dict]:
        """ Creates a discussion in the backend service.

        Args:
            - backendservice (BackendService): The backend service.
            - title (str): The title of the discussion to be created.
            - content (str): The content of the discussion to be created.

        Returns:
            - Dict: A dictionary with the newly created user if successful.
            - None: Nothing on error.
        """
        response: ResponseData = backend_service.create_discussion(session.get('token'), title, content)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def get_discussion(backend_service: BackendService, discussionid: int) -> Optional[Dict]:
        response: ResponseData = backend_service.get_discussion(session.get('token'), discussionid)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def list_reports(backend_service:BackendService) -> List:
        """ Gets the list of discussions from the backend service.

        Args:
            - backend_service (BackendService): The backend service.

        Returns:
            - List: A list of user data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_reports(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def get_report(backend_service: BackendService, id: int) -> Optional[Dict]:
        response: ResponseData = backend_service.get_report(session.get('token'), id)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def list_reports_answer(backend_service:BackendService) -> List:
        """ Gets the list of discussions from the backend service.

        Args:
            - backend_service (BackendService): The backend service.

        Returns:
            - List: A list of user data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_reports_answer(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def list_reports_comments(backend_service:BackendService) -> List:
        """ Gets the list of discussions from the backend service.

        Args:
            - backend_service (BackendService): The backend service.

        Returns:
            - List: A list of user data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_reports_comments(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def put_report(backend_service: BackendService, id: int) -> Optional[Dict]:
        status ="ACCEPTED"
        response: ResponseData = backend_service.put_report(session.get('token'), id,status)
        WebUtils.flash_response_messages(response)
        return response.get_content()