""" reportServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db import Schema
from dms2223backend.data.db.results import Report
from dms2223backend.logic import ReportLogic


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
                out['id'] = report.id
                out['title'] = report.title      
                out['content'] = report.content
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out

    @staticmethod
    def list_reports(schema: Schema) -> List[Dict]: # pasar por parametro discussionid: int 
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
                'id': report.id,
                'discussionid': report.discussionid,
                'content': report.content,
            })
        schema.remove_session()
        return out

    @staticmethod
    def create_report(title:str, content: str, schema: Schema) -> Dict:
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
            new_report: Report = ReportLogic.create(session, title, content)
            
            out['id'] = new_report.id
            out['title'] = new_report.title
            out['content'] = new_report.content

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out
