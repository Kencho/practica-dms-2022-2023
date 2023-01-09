"""Answer Class Module
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer ,ForeignKey # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.db.results.reportanswer import Reportanswer
from dms2223backend.data.db.results.comment import Comment

from dms2223backend.data.db.results.voteAnswer import VoteAnswer

class Answer(ResultBase):
    """ Definition and storage of answer ORM records.
    """

    def __init__(self, discussionid: int, content: str):
        """ Constructor method.

        Initializes a answer record.

        Args:
            - user (str): A string with the user's name.
            - id (int): A int with the discussion's id.

        """
        
        self.discussionid: int = discussionid
        #self.user: str = user
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
            'answers',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('discussionid', Integer, ForeignKey('discussions.id'), nullable=False),
            Column('content', String(250), nullable=False)
          
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.

        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {
            'answers': relationship(Comment, backref='answer'),
            'reportanswer': relationship(Reportanswer , backref="answer"),
            'vote': relationship(VoteAnswer,backref="answer" )
        }
