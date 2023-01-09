""" REST API controllers responsible of handling the answer operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.data.db.exc import DiscussionNotFoundError
from dms2223backend.logic.exc.operationerror import OperationError
from dms2223backend.service import AnswersServices



def answer(body: Dict, id: int) -> Tuple[Union[Dict, str], Optional[int]]:
    """Answers a discussion if the requestor has the discussion role.

    Args:
        - body (Dict): A dictionary with the new discussion's data.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Optional[str], Optional[int]]: On success, a tuple with the dictionary of the
          new discussion data and a code 200 OK. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
            - 403 FORBIDDEN when the requestor does not have the rights to create the discussion.
            - 409 CONFLICT if an existing user already has all or part of the unique user's data.
    """
    with current_app.app_context():
        try:
            answer = AnswersServices.answer(
                id, body['content'], current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except DiscussionNotFoundError:
            return('User does not exist', HTTPStatus.NOT_FOUND.value)
        except OperationError:
            return ('The user with the given username can not create a discussion', HTTPStatus.FORBIDDEN.value)
    return (answer, HTTPStatus.OK.value)


def list_all_for_discussion(id: int) -> Tuple[Union[List[Dict], str], Optional[int]]:
    """Lists the answers of a discussion if the requestor has the discussion role.

    Args:
        - disucssionId (int): Discussion id.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Union[List[Dict], str], Optional[int]]: On success, a tuple with the dictionary of the
          new discussion data and a code 200 OK. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
    """
    with current_app.app_context():
        try:
            answers: List[Dict] = AnswersServices.list_all_for_discussion(
                id, current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)

    return (answers, HTTPStatus.OK.value)



def get_answer(discussionid: int) -> Tuple[Union[Dict, str], Optional[int]]:
    """Obtains the answer of a discussion and user.

    Args:
        - username (str): Username string.
        - id: Discussion id.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new discussion data and a code 200 OK. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
    """
    with current_app.app_context():
        try:
            answer: Dict = AnswersServices.get_answer(
                discussionid,current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)

    return (answer, HTTPStatus.OK.value)



def vote_answer(id: int) -> Tuple[Dict, int]:
    """vOTE an answer

    Args:
        - id: answer id.
        

    Returns:
        - Tuple[Dict, str]]: On success, a tuple with the dictionary of the
          answer data and a code 200 OK. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
    """
    with current_app.app_context():
        try:
            vote = AnswersServices.vote_answer(id,current_app.db)
            
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)

    return (HTTPStatus.OK.value)