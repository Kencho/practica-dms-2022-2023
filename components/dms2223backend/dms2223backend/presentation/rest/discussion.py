""" REST API controllers responsible of handling the discussion operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.logic.exc.operationerror import OperationError
from dms2223backend.service import DiscussionsServices

def list_discussions() -> Tuple[List[Dict], Optional[int]]:
    """Lists the existing discussions.

    Returns:
        - Tuple[List[Dict], Optional[int]]: A tuple with a list of dictionaries for the discussions' data
          and a code 200 OK.
    """
    with current_app.app_context():
        discussions: List[Dict] = DiscussionsServices.list_discussions(current_app.db)
    return (discussions, HTTPStatus.OK.value)


def create_discussion(body: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    """Creates a discussion if the requestor has the discussion role.

    Args:
        - body (Dict): A dictionary with the new discussion's data.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new user data and a code 201 CREATED. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
            - 403 FORBIDDEN when the requestor does not have the rights to create the discussion.
            - 409 CONFLICT if an existing user already has all or part of the unique user's data.
    """
    with current_app.app_context():
        try:
            discussion: Dict = DiscussionsServices.create_discussion(
                body['title'], body['content'],current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except OperationError:
            return ('The user with the given username can not create a discussion', HTTPStatus.FORBIDDEN.value)
    return (discussion, HTTPStatus.OK.value)

def get_discussion_by_id(id: int) -> Tuple[Union[Dict, str], Optional[int]]:
    """Get a discussion by id.

    Args:
        - id (int): Id for discussion.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new discussion data and a code 200 OK. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
    """
    with current_app.app_context():
        try:
            discussion: Dict = DiscussionsServices.get_discussion_by_id(
               id, current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
    return (discussion, HTTPStatus.OK.value)
