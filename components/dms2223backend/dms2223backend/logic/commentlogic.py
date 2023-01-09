""" CommentLogic class module.
"""

from typing import List
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db.results import Comment
from dms2223backend.data.db.resultsets import Comments

from dms2223backend.data.db.results import VoteComment
class CommentLogic():
    """ Class responsible of table-level comments operations.
    """
    @staticmethod
    def comment(session: Session, discussionid: int, answerid: int, content: str) -> Comment:
        """ Comment a comment.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - username (str): The username of the comment string.
            - discussionId (str): Id of the discussion.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `Discussion` result.
        """
        try:
            new_comment: Comment = Comments.comment(session, discussionid, answerid, content)
           
        except Exception as ex:
            raise ex
        return new_comment

    @staticmethod
    def list_all(session: Session) -> List[Comment]:
        """Lists every comment.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Comment]: A list of `Comment` registers.
        """

        return Comments.list_all(session)

    @staticmethod
    def list_all_for_discussion(discussionid: int, session: Session) -> List[Comment]:
        """Lists the `answers made to a certain question.

        Args:
            - session (Session): The session object.
            - id (int): The question id.

        Raises:
            - ValueError: If the question id is missing.

        Returns:
            - List[Answer]: A list of answer registers with the question answers.
        """
        return Comments.list_all_for_discussion(session, discussionid)

    @staticmethod
    def list_all_for_answer(answerid: int, session: Session) -> List[Comment]:
        """Lists the `answers made to a certain question.

        Args:
            - session (Session): The session object.
            - id (int): The question id.

        Raises:
            - ValueError: If the question id is missing.

        Returns:
            - List[Answer]: A list of answer registers with the question answers.
        """
        return Comments.list_all_for_answer(session, answerid)

    @staticmethod
    def get_comment(session: Session, discussionid: int, answerid: int) -> Comment:
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Returns:
            - Answer: The Answer of the question.
        """
        try:
            comment: Comment = Comments.get_comment(session, discussionid, answerid)
        except Exception as ex:
            raise ex
        return comment

    @staticmethod
    def vote_comment(session: Session, cid: int ):
        """Vote an Answer

        Args:
            
            - aid: answer id.
            

        Returns:
            - Dict: Answer of the discussion.
        """

        try:
            vote: VoteComment = VoteComment(cid)
            session.add(vote)
            session.commit()
        except Exception as ex:
            raise ex
        return vote

    @staticmethod
    def get_vote(session: Session ,commentid: int) :
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Returns:
            - Answer: The Answer of the question.
        """
        try:
            vote: int = Comments.get_vote(session, commentid)
        except Exception as ex:
            raise ex
        return vote
    