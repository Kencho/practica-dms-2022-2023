"""Discussion Class Module
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, TIME, DATE # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.db.results.answer import Answer
from dms2223backend.data.db.results.comment import Comment
from dms2223backend.data.db.results.report import Report

class Discussion(ResultBase):
    """ Definition and storage of discussion ORM records.
    """

    def __init__(self, title: str, content: str):
        """ Constructor method.

        Initializes a discussion record.

        Args:
            - title (str): A string with the discussion title.
            - content (str): A string with the discussion title.
        """

      
        self.title: str = title
        self.content: str = content

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
            'discussions',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('title', String(50), nullable=False),
            Column('content', String(250), nullable=False)
            #Column('time', TIME, nullable = False),
            #Column('user', String(15), nullable=False),
            #Column('date', DATE, nullable = False)
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.

        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {
            'discussions': relationship(Answer,backref='discussion'),
            'reports': relationship(Report,backref='discussion')
        }
