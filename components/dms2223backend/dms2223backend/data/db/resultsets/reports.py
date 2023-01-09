""" reports class module.
"""

import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Report
from dms2223backend.data.db.results import Reportanswer
from dms2223backend.data.db.exc import ReportExistsError
from dms2223backend.data.db.results import Reportcomment
from dms2223backend.data.reportstatus import ReportStatus

class Reports():
    """ Class responsible of table-level reports operations.
    """
    @staticmethod
    def create(session: Session,discussionid: int,reason: str) -> Report:
        """ Creates a new report record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - title (str): The title of the report string.
            - content (str): The content of the report string.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `report` result.
        """
        if not reason:
            raise ValueError('A type report and a content hash are required.')
        try:
            estado = ReportStatus.PENDING
            new_report = Report(discussionid,reason,estado)
            session.add(new_report)
            session.commit()
            return new_report
        except IntegrityError as ex:
            raise ReportExistsError(
                'A report with name already exists.'
                ) from ex

    @staticmethod
    def create_answer_report(session: Session,answerid: int,reason: str) -> Report:
        """ Creates a new report record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - title (str): The title of the report string.
            - content (str): The content of the report string.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `report` result.
        """
        if not reason:
            raise ValueError('A type report and a content hash are required.')
        try:
            estado = ReportStatus.PENDING
            new_report = Reportanswer(answerid,reason,estado)
            session.add(new_report)
            session.commit()
            return new_report
        except IntegrityError as ex:
            raise ReportExistsError(
                'A report with name already exists.'
                ) from ex

    @staticmethod
    def create_comment_report(session: Session,commentid: int,reason: str) -> Report:
        """ Creates a new report record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - title (str): The title of the report string.
            - content (str): The content of the report string.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `report` result.
        """
        if not reason:
            raise ValueError('A type report and a content hash are required.')
        try:
            estado = ReportStatus.PENDING
            new_report = Reportcomment(commentid,reason,estado)
            session.add(new_report)
            session.commit()
            return new_report
        except IntegrityError as ex:
            raise ReportExistsError(
                'A report with name already exists.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[Report]:
        """Lists every report.

        Args:
            - session (Session): The session object.

        Returns:
            - List[report]: A list of `report` registers.
        """
        query = session.query(Report)
        return query.all()

    @staticmethod
    def list_all_report_answer(session: Session) -> List[Report]:
        """Lists every report.

        Args:
            - session (Session): The session object.

        Returns:
            - List[report]: A list of `report` registers.
        """
        query = session.query(Reportanswer)
        return query.all()

    @staticmethod
    def list_all_report_comments(session: Session) -> List[Report]:
        """Lists every report.

        Args:
            - session (Session): The session object.

        Returns:
            - List[report]: A list of `report` registers.
        """
        query = session.query(Reportcomment)
        return query.all()

    @staticmethod
    def get_report_by_id(session: Session, id: int,) -> Optional[Report]:
        """Obtains a report by an id.
        Args:
            - session (Session): The session object.
            - id (int): Id report integer.

        Returns:
            - Optional[report]: The result of the `report`.
        """

        if not id:
            raise ValueError('An id is requiered.')
        try:
            query = session.query(report).filter_by(id=id)
            report: report = query.one()
        except NoResultFound:
            return None
        return report
