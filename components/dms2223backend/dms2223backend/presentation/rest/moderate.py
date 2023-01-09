""" REST API controllers responsible of handling the report operations.
"""

from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.logic.exc.operationerror import OperationError
from dms2223backend.service import reportsServices

def list_reports() -> Tuple[List[Dict], Optional[int]]:
    """Lists the existing reports.

    Returns:
        - Tuple[List[Dict], Optional[int]]: A tuple with a list of dictionaries for the reports' data
          and a code 200 OK.
    """
    with current_app.app_context():
        reports: List[Dict] = reportsServices.list_reports(current_app.db)
    return (reports, HTTPStatus.OK.value)

def list_reports_answer() -> Tuple[List[Dict], Optional[int]]:
    """Lists the existing reports.

    Returns:
        - Tuple[List[Dict], Optional[int]]: A tuple with a list of dictionaries for the reports' data
          and a code 200 OK.
    """
    with current_app.app_context():
        reports: List[Dict] = reportsServices.list_reports_answer(current_app.db)
    return (reports, HTTPStatus.OK.value)

def list_reports_comments() -> Tuple[List[Dict], Optional[int]]:
    """Lists the existing reports.

    Returns:
        - Tuple[List[Dict], Optional[int]]: A tuple with a list of dictionaries for the reports' data
          and a code 200 OK.
    """
    with current_app.app_context():
        reports: List[Dict] = reportsServices.list_reports_comments(current_app.db)
    return (reports, HTTPStatus.OK.value)

def create_report(body: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    """Creates a report if the requestor has the report role.

    Args:
        - body (Dict): A dictionary with the new report's data.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new user data and a code 201 CREATED. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
            - 403 FORBIDDEN when the requestor does not have the rights to create the report.
            - 409 CONFLICT if an existing user already has all or part of the unique user's data.
    """
    with current_app.app_context():
        try:
            
            report: Dict = reportsServices.create_report(
                body['tiporeport'],body['title'],body['content'],current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except OperationError:
            return ('The user with the given username can not create a report', HTTPStatus.FORBIDDEN.value)
    return (report, HTTPStatus.OK.value)

def create_comment_report(body: Dict, id: int ) -> Tuple[Union[Dict, str], Optional[int]]:
    """Creates a report if the requestor has the report role.

    Args:
        - body (Dict): A dictionary with the new report's data.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new user data and a code 201 CREATED. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
            - 403 FORBIDDEN when the requestor does not have the rights to create the report.
            - 409 CONFLICT if an existing user already has all or part of the unique user's data.
    """
    with current_app.app_context():
        try:
            report: Dict = reportsServices.create_report_comment(
                id,body['reason'],current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except OperationError:
            return ('The user with the given username can not create a report', HTTPStatus.FORBIDDEN.value)
    return (report, HTTPStatus.OK.value)

def create_answer_report(body: Dict, id: int ) -> Tuple[Union[Dict, str], Optional[int]]:
    """Creates a report if the requestor has the report role.

    Args:
        - body (Dict): A dictionary with the new report's data.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new user data and a code 201 CREATED. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
            - 403 FORBIDDEN when the requestor does not have the rights to create the report.
            - 409 CONFLICT if an existing user already has all or part of the unique user's data.
    """
    with current_app.app_context():
        try:
            report: Dict = reportsServices.create_report_answer(
                id,body['reason'],current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except OperationError:
            return ('The user with the given username can not create a report', HTTPStatus.FORBIDDEN.value)
    return (report, HTTPStatus.OK.value)

def create_report(body: Dict, id: int ) -> Tuple[Union[Dict, str], Optional[int]]:
    """Creates a report if the requestor has the report role.

    Args:
        - body (Dict): A dictionary with the new report's data.
        - token_info (Dict): A dictionary of information provided by the security schema handlers.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new user data and a code 201 CREATED. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
            - 403 FORBIDDEN when the requestor does not have the rights to create the report.
            - 409 CONFLICT if an existing user already has all or part of the unique user's data.
    """
    with current_app.app_context():
        try:
            report: Dict = reportsServices.create_report(
                id,body['reason'],current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
        except OperationError:
            return ('The user with the given username can not create a report', HTTPStatus.FORBIDDEN.value)
    return (report, HTTPStatus.OK.value)

def get_report_by_id(id: int) -> Tuple[Union[Dict, str], Optional[int]]:
    """Get a report by id.

    Args:
        - id (int): Id for report.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new report data and a code 200 OK. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
    """
    with current_app.app_context():
        try:
            report: Dict = reportsServices.get_report_by_id(
               id, current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
    return (report, HTTPStatus.OK.value)

def update_report_status(body : Dict , id : int) -> Tuple[Union[Dict, str], Optional[int]]:
    """Get a report by id.

    Args:
        - id (int): Id for report.

    Returns:
        - Tuple[Union[Dict, str], Optional[int]]: On success, a tuple with the dictionary of the
          new report data and a code 200 OK. On error, a description message and code:
            - 400 BAD REQUEST when a mandatory argument is missing.
    """
    with current_app.app_context():
        try:
            reportsServices.update_report_status(current_app.db , id , body['status'])
            reporte: Dict = reportsServices.get_report_by_id(id,current_app.db) #cambiar
            return reporte , HTTPStatus.OK

        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)
    return (report, HTTPStatus.OK.value)