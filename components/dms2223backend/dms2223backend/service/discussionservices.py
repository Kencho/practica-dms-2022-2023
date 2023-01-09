""" DiscussionServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db import Schema
from dms2223backend.data.db.results import Discussion
from dms2223backend.logic import DiscussionLogic


class DiscussionsServices():
    """ Monostate class that provides high-level services to handle user-related use cases.
    """
    @staticmethod
    def get_discussion_by_id(id: int, schema: Schema) -> Dict:
        """Determines whether a user with the given credentials exists.

        Args:
            - schema (Schema): A database handler where the discussions are mapped into.
            - id (int): Discussion id.

        Returns:
            - Dict: Dictonary that contains the discussions's data.
        """
      
        session: Session = schema.new_session()
        out:  List[Dict] = []
        try:
            discussions = DiscussionLogic.get_discussion_by_id(session, id)
            discussion: Discussion = discussions[0][0]
            answered: int = discussions[0][1]
            if discussion is not None:
                out.append({
                'id': discussion.id,#type: ignore
                'title': discussion.title,
                'content': discussion.content,
                'answered': answered})

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        salida : Dict = {}
        for sal in out:
            salida = sal
        return salida

    @staticmethod
    def list_discussions(schema: Schema) -> List[Dict]:
        """Lists the existing discussions.

        Args:
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - List[Dict]: A list of dictionaries with the discussions' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        discussions: List[List] = DiscussionLogic.list_all(session)
        for discuss in discussions:
            discussion: Discussion = discuss[0]
            answered: int = discuss[1]
            out.append({
                'id': discussion.id,#type: ignore
                'title': discussion.title,
                'content': discussion.content,
                'answered': answered
            })
        schema.remove_session()
        return out

    @staticmethod
    def create_discussion(title:str, content: str, schema: Schema) -> Dict:
        """Creates a discussion.

        Args:
            - schema (Schema): A database handler where the discussions are mapped into.
            - id (int): Discussion id.

        Returns:
            - Dict: Dictonary that contains the discussions's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_discussion: Discussion = DiscussionLogic.create(session, title, content)
            
            out['id'] = new_discussion.id#type: ignore
            out['title'] = new_discussion.title
            out['content'] = new_discussion.content

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out
