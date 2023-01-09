""" Comments class module.
"""

from typing import List
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db.results import Comment, VoteComment
from dms2223backend.data.db.exc import DiscussionNotFoundError

class Comments():
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
        if not answerid or not content or not discussionid:
            raise ValueError('An content and an Id hash are required.')
        try:
            new_comment = Comment(discussionid, answerid, content)
            session.add(new_comment)
            session.commit()
            return new_comment
        except IntegrityError as ex:
            raise DiscussionNotFoundError(
                'An answer with id ' + str(answerid) + ' not exists.'
                ) from ex
                
    @staticmethod
    def list_all(session: Session) -> List[Comment]:
        """Lists every comment.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Comment]: A list of `Comment` registers.
        """
        query = session.query(Comment)
        return query.all()

    @staticmethod
    def answer_has_comments(session: Session, answerid: int) -> bool:
        if not answerid:
            raise ValueError('An answer id is required.')
        answers = Comments.list_all_for_answer(session, answerid)

        return len(answers) != 0

    @staticmethod
    def list_all_for_discussion(session: Session, discussionid: int) -> List[Comment]:
        """Lists the `answers made to a certain question.

        Args:
            - session (Session): The session object.
            - id (int): The question id.

        Raises:
            - ValueError: If the question id is missing.

        Returns:
            - List[Answer]: A list of answer registers with the question answers.
        """
        if not discussionid:
            raise ValueError('An answer id is required')
        query = session.query(Comment).filter_by(discussionid=discussionid)
        return query.all()

    @staticmethod
    def list_all_for_answer(session: Session, answerid: int) -> List[Comment]:
        """Lists the `answers made to a certain question.

        Args:
            - session (Session): The session object.
            - id (int): The question id.

        Raises:
            - ValueError: If the question id is missing.

        Returns:
            - List[Answer]: A list of answer registers with the question answers.
        """
        if not answerid:
            raise ValueError('An answer id is required')
        query = session.query(Comment).filter_by(answerid=answerid)
        return query.all()
        
    @staticmethod
    def get_comment(session: Session, discussionid: int, answerid: int) -> Comment:
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Raises:
            - ValueError: If the username is missing.

        Returns:
            - Answer: Answer of the question.
        """
        if not answerid or not discussionid:
            raise ValueError('All fields are required.')
        query = session.query(Comment).filter_by(
            discussionid=discussionid, answerid=answerid
        )
        return query.all()
        
    @staticmethod
    def get_vote(session: Session, commentid: int) -> Comment:
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Raises:
            - ValueError: If the username is missing.

        Returns:
            - Answer: Answer of the question.
        """
        if not commentid:
            raise ValueError('All fields are required.')
        query = session.query(VoteComment).filter_by(
            cid=commentid
        )
        
        return query.count() 
        