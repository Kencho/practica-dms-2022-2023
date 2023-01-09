"""report Class Module
"""

from typing import Dict
from sqlalchemy import Table, MetaData,Enum ,DateTime,Column,func ,String , Integer, TIME, DATE ,ForeignKey# type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.db.results.answer import Answer
from dms2223backend.data.reportstatus import ReportStatus


class Report(ResultBase):
    """ Definition and storage of report ORM records.
    """

    def __init__(self,discussionid:int ,reason: str,status:ReportStatus):
        """ Constructor method.

        Initializes a report record.

        Args:
            - title (str): A string with the report title.
            - content (str): A string with the report title.
        """

    
        #self.tipo: int = tipo
        self.reason: str = reason
        self.discussionid: int = discussionid
        self.status: ReportStatus = status
        self.timestamp: DateTime
        #self.propietario: str = usuario
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
            'reports',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('reason', String(250), nullable=False),
            Column('discussionid', Integer, ForeignKey('discussions.id'), nullable=False),
            Column('tipo', Integer ,nullable=True), # si vale 1 discusion , si vale 2 respuesta , si vale 3 comentario
            Column('status',Enum(ReportStatus),default = ReportStatus.PENDING ,nullable = False),
            #Column('propietario', String(250), nullable=False),
            Column('timestamp', DateTime, nullable=False, default = func.now())
        )


