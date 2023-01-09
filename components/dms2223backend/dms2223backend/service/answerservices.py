""" AnswerServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db import Schema
from dms2223backend.data.db.results import Answer
from dms2223backend.logic import AnswerLogic


class AnswersServices():
    """ Monostate class that provides high-level services to handle user-related use cases.
    """
    @staticmethod
    def answer(discussionid: int, content: str, schema: Schema) -> Dict:
        """Answers a discussion.

        Args:
            - username (str): Username string.
            - discussionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - Dict: Dictonary that contains the answer's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_answer: Answer = AnswerLogic.answer(session, discussionid, content)
            
            out['id'] = new_answer.id #type: ignore
            out['discussionid'] = new_answer.discussionid
            out['content'] = new_answer.content

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out



    @staticmethod
    def list_all_for_discussion(discussionid: int, schema: Schema) -> List[Dict]:
        """Lists the answers of a discussion if the requestor has the discussion role.

        Args:
            - disucssionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - List[Dict]: List of dictionaries with the answers' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        answers: List[Answer] = AnswerLogic.list_all_for_discussion(discussionid,session)
        
        for answer in answers:
            vote = AnswerLogic.get_vote(session, answer.id)
            out.append({
                'id': answer.id, #type: ignore
                'discussionid': answer.discussionid,
                'content': answer.content,
                'vote': vote
            })
        schema.remove_session()
        return out

    @staticmethod
    def get_answer(discussionid: int, schema: Schema) -> Dict:
        """Obtains the answer of a discussion and user.

        Args:
            - username (str): Username string.
            - discussionid: Discussion id.
            

        Returns:
            - Dict: Answer of the discussion.
        """
        
        session: Session = schema.new_session()
        out: Dict = {}
        answer: Answer = AnswerLogic.get_answer(session, discussionid)
        out['id'] = answer.id #type: ignore
        out['discussionid'] = answer.discussionid
        out['content'] = answer.content
        schema.remove_session()
        return out

    @staticmethod
    def vote_answer(aid: int, schema: Schema):
        """Vote an Answer

        Args:
            
            - aid: answer id.
            

        Returns:
            - Dict: Answer of the discussion.
        """
        
        session: Session = schema.new_session()
        
        vote: Answer = AnswerLogic.vote_answer(session, aid)
   
        schema.remove_session()
        return True