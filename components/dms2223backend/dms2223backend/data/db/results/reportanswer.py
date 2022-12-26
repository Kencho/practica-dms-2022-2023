"""report Class Module
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, TIME, DATE ,ForeignKey# type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase


class Reportanswer(ResultBase):
    """ Definition and storage of report ORM records.
    """

    def __init__(self, answerid:int ,reason: str):
        """ Constructor method.

        Initializes a report record.

        Args:
            - title (str): A string with the report title.
            - content (str): A string with the report title.
        """


        self.reason: str = reason
        self.answerid: int = answerid
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
            'reportsanswer',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('reason', String(250), nullable=False),
            Column('answerid', Integer, ForeignKey('answers.id'), nullable=False),
            Column('tipo', Integer ,nullable=True), # si vale 1 discusion , si vale 2 respuesta , si vale 3 comentario
            #Column('time', TIME, nullable = False),
            #Column('user', String(15), nullable=False),
            #Column('date', DATE, nullable = False)
        )
