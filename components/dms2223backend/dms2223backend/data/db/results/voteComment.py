from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer ,ForeignKey # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase




class VoteComment(ResultBase):
    """ Definition and storage of answer ORM records.
    """

    def __init__(self, cid: int):
        """ Constructor method.

        Initializes a answer record.

        Args:
            - user (str): A string with the user's name.
            - id (int): A int with the discussion's id.

        """
        
    
        
        self.cid: int = cid
        
        
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
            'votecomments',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('cid', Integer, ForeignKey('comments.id'), nullable=False),
        )

