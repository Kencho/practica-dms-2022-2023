""" reportServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db import Schema
from dms2223backend.data.reportstatus import ReportStatus
from dms2223backend.data.db.results import Report, Reportcomment , Reportanswer
from dms2223backend.logic import ReportLogic , DiscussionLogic
from dms2223backend.data.db.results.discussion import Discussion


class reportsServices():
    """ Monostate class that provides high-level services to handle user-related use cases.
    """
    @staticmethod
    def get_report_by_id(id: int, schema: Schema) -> Dict:
        """Determines whether a user with the given credentials exists.

        Args:
            - schema (Schema): A database handler where the reports are mapped into.
            - id (int): report id.

        Returns:
            - Dict: Dictonary that contains the reports's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            report = ReportLogic.get_report_by_id(session, id)
            if report is not None:
                out['id'] = report.id # type: ignore
                out['title'] = report.title # type: ignore
                out['content'] = report.content # type: ignore
               # out['user'] = report.user
                
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out

    @staticmethod
    def list_reports(schema: Schema) -> List[Dict]: 
        """Lists the existing reports.

        Args:
            - schema (Schema): A database handler where the reports are mapped into.

        Returns:
            - List[Dict]: A list of dictionaries with the reports' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        reports: List[List] = ReportLogic.list_all(session)
        for report in reports:
            out.append({
                'id': report.id, # type: ignore
                'discussionid': report.discussionid, # type: ignore
                'reason': report.reason, # type: ignore
                'timestamp': report.timestamp, # type: ignore
                'status': report.status.name # type: ignore
                #'user': report.user
            })
        schema.remove_session()
        return out

    @staticmethod
    def list_reports_answer(schema: Schema) -> List[Dict]: 
        """Lists the existing reports.

        Args:
            - schema (Schema): A database handler where the reports are mapped into.

        Returns:
            - List[Dict]: A list of dictionaries with the reports' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        reports: List[List] = ReportLogic.list_all_report_answer(session)
        for report in reports:
            out.append({
                'id': report.id, # type: ignore
                'answerid': report.answerid, # type: ignore
                'reason': report.reason, # type: ignore
                'timestamp': report.timestamp, # type: ignore
                'status': report.status.name # type: ignore
                #'user': report.user 
            })
        schema.remove_session()
        return out

    @staticmethod
    def list_reports_comments(schema: Schema) -> List[Dict]: 
        """Lists the existing reports.

        Args:
            - schema (Schema): A database handler where the reports are mapped into.

        Returns:
            - List[Dict]: A list of dictionaries with the reports' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        reports: List[List] = ReportLogic.list_all_report_comments(session)
        for report in reports:
            out.append({
                'id': report.id, # type: ignore
                'commentid': report.commentid, # type: ignore
                'reason': report.reason, # type: ignore
                'timestamp': report.timestamp, # type: ignore
                'status': report.status.name # type: ignore
                #'user': report.user
            })
        schema.remove_session()
        return out

    @staticmethod
    def create_report(id:int, reason: str  ,schema: Schema) -> Dict:
        """Creates a report.

        Args:
            - schema (Schema): A database handler where the reports are mapped into.
            - id (int): report id.

        Returns:
            - Dict: Dictonary that contains the reports's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_report: Report = ReportLogic.create(session, id, reason)
            out['id'] = new_report.id #type: ignore
            out['reason'] = new_report.reason
            out['tipo'] = new_report.tipo # type: ignore
            out['timestamp'] = new_report.timestamp
            out['discussionid'] = new_report.discussionid
            out['status'] = new_report.status.name
            #out['user'] = new_report.user

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out

    @staticmethod
    def create_report_comment(id:int, reason: str  ,schema: Schema) -> Dict:
        """Creates a report.

        Args:
            - schema (Schema): A database handler where the reports are mapped into.
            - id (int): report id.

        Returns:
            - Dict: Dictonary that contains the reports's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_report: Reportcomment = ReportLogic.create_report_comment(session, id, reason)
            out['id'] = new_report.id #type: ignore
            out['reason'] = new_report.reason
            out['tipo'] = new_report.tipo # type: ignore
            out['commentid'] = new_report.commentid
            out['status'] = new_report.status.name
            #out['user'] = new_report.user

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out

    @staticmethod
    def create_report_answer(id:int, reason: str  ,schema: Schema) -> Dict:
        """Creates a report.

        Args:
            - schema (Schema): A database handler where the reports are mapped into.
            - id (int): report id.

        Returns:
            - Dict: Dictonary that contains the reports's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_report: Reportanswer = ReportLogic.create_report_answer(session, id, reason)
            out['id'] = new_report.id #type: ignore
            out['reason'] = new_report.reason
            out['tipo'] = new_report.tipo # type: ignore
            out['answerid'] = new_report.answerid 
            out['status'] = new_report.status.name
            #out['user'] = new_report.user

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out

    @staticmethod
    def update_report_status(schema: Schema, id: int , status: str):
        session: Session = schema.new_session()

        reporte : ReportLogic = ReportLogic.get_report_by_id(session , id)
        reporte.status = ReportStatus[status]
        if status == 'ACCEPTED':
            reportsServices.quitar_discusion(schema. reporte.id)

            session.add(reporte)
            session.commit()

            schema.remove_session()

    @staticmethod
    def quitar_discusion(schema: Schema, id: int):
        session : Session = schema.new_session()

        discussion: Discussion = DiscussionLogic.get_discussion_by_id(session, id)

        session.add(discussion)
        session.commit()
        schema.remove_session()