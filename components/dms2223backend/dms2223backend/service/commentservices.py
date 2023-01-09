""" CommentServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db import Schema
from dms2223backend.data.db.results import Comment
from dms2223backend.logic import CommentLogic

class CommentsServices():
    """ Monostate class that provides high-level services to handle user-related use cases.
    """
    @staticmethod
    def comment(discussionid: int, answerid: int, content: str, schema: Schema) -> Dict:
        """Comments an answer.

        Args:
            - discussionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - Dict: Dictonary that contains the answer's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_comment: Comment = CommentLogic.comment(session, discussionid, answerid, content)
            
            out['id'] = new_comment.id #type: ignore
            out['discussionid'] = new_comment.discussionid 
            out['answerid'] = new_comment.answerid
            out['content'] = new_comment.content

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out

    @staticmethod
    def list_all_for_discussion(discussionid: int, schema: Schema) -> List[Dict]:
        """Lists the comments of a discussion if the requestor has the discussion role.

        Args:
            - disucssionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - List[Dict]: List of dictionaries with the comments' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        comments: List[Comment] = CommentLogic.list_all_for_discussion(discussionid, session)
        for comment in comments:
            vote = CommentLogic.get_vote(session, comment.id)
            out.append({
                'id': comment.id, #type: ignore
                'discussionid': comment.discussionid,
                'answerid': comment.answerid,
                'content': comment.content,
                'vote': vote
            })
        schema.remove_session()
        return out

    @staticmethod
    def list_all_for_answer(answerid: int, schema: Schema) -> List[Dict]:
        """Lists the comments of a discussion if the requestor has the discussion role.

        Args:
            - disucssionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - List[Dict]: List of dictionaries with the comments' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        comments: List[Comment] = CommentLogic.list_all_for_answer(answerid, session)
        for comment in comments:
            out.append({
                'id': comment.id, #type: ignore
                'discussionid': comment.discussionid,
                'answerid': comment.answerid,
                'content': comment.content
            })
        schema.remove_session()
        return out

    @staticmethod
    def get_comment(discussionid: int, answerid: int, schema: Schema) -> Dict:
        """Obtains the comment of a discussion and user.

        Args:
            - username (str): Username string.
            - id: Discussion id.
            - token_info (Dict): A dictionary of information provided by the security schema handlers.

        Returns:
            - Dict: Comment of the answer.
        """
        session: Session = schema.new_session()
        out: Dict = {}
        comment: Comment = CommentLogic.get_comment(session, discussionid, answerid)
        out['id'] = comment.id #type: ignore
        out['discussionid'] = comment.discussionid #type: ignore
        out['answerid'] = comment.answerid
        out['content'] = comment.content
        schema.remove_session()
        return out

    @staticmethod
    def vote_comment(cid: int, schema: Schema):
        """Vote an cooment

        Args:
            
            - cid: comment id.
            

        Returns:
            - Dict: Answer of the discussion.
        """
        
        session: Session = schema.new_session()
        
        vote: Comment = CommentLogic.vote_comment(session, cid)
   
        schema.remove_session()
        return True
