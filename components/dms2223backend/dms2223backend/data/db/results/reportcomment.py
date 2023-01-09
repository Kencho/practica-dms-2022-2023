"""report Class Module
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, func ,DateTime,String ,Enum, Integer, TIME, DATE ,ForeignKey# type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.reportstatus import ReportStatus

class Reportcomment(ResultBase):
    """ Definition and storage of report ORM records.
    """

    def __init__(self,commentid:int ,reason: str,status:ReportStatus):
        """ Constructor method.

        Initializes a report record.

        Args:
            - title (str): A string with the report title.
            - reason (str): A string with the report title.
        """

    
        self.reason: str = reason
        self.commentid: int = commentid
        self.timestamp: DateTime
        self.status: ReportStatus = status

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.

        Args:
            - metadata (MetaData): The database schema metadata
                        (used to gather the entities' definitions and mapping)

        Returns:
            - Table: A `Table` object with the table definition.
        """
        return Table(
            'reportscomment',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('reason', String(250), nullable=False),
            Column('commentid', Integer, ForeignKey('comments.id'), nullable=False),
            Column('status',Enum(ReportStatus),default = ReportStatus.PENDING ,nullable = False),
            Column('timestamp', DateTime, nullable=False, default = func.now())
            #Column('user', String(15), nullable=False),
            #Column('date', DATE, nullable = False)
        )
