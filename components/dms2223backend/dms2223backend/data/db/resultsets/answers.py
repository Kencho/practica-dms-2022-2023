""" Answers class module.
"""

import hashlib
from typing import List
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Answer, VoteAnswer
from dms2223backend.data.db.exc.discussionnotfounderror import DiscussionNotFoundError


class Answers():
    """ Class responsible of table-level answers operations.
    """
    @staticmethod
    def answer(session: Session, discussionid: int, content: str) -> Answer:
        """ Answers a discussion.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - username (str): The username of the answer string.
            - discussionId (str): Id of the discussion.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `Discussion` result.
        """
        if not discussionid or not content:
            raise ValueError('An content and an Id hash are required.')
        try:
            new_answer = Answer(discussionid, content)
            session.add(new_answer)
            session.commit()
            return new_answer
        except IntegrityError as ex:
            raise DiscussionNotFoundError(
                'A discussion with id ' + str(discussionid) + ' not exists.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[Answer]:
        """Lists every answer.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Answer]: A list of `Answer` registers.
        """
        
        query = session.query(Answer)
        return query.all()

    @staticmethod
    def discussion_has_answers(session: Session, discussionid: int) -> bool:
        if not discussionid:
            raise ValueError('A discussion id is required.')
        discussions = Answers.list_all_for_discussion(session, discussionid)

        return len(discussions) != 0

    @staticmethod
    def list_all_for_discussion(session: Session, discussionid: int) -> List[Answer]:
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
            raise ValueError('A discussion id is required')
        query = session.query(Answer).filter_by(discussionid=discussionid)
        return query.all()

    @staticmethod
    def get_answer(session: Session, answerid: int) -> Answer:
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
        if not answerid:
            raise ValueError('All fields are required.')
        query = session.query(Answer).filter_by(
            answerid=answerid
        )
        return query.all()

    @staticmethod
    def get_vote(session: Session, answerid: int) -> Answer:
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
        if not answerid:
            raise ValueError('All fields are required.')
        query = session.query(VoteAnswer).filter_by(
            aid=answerid
        )
        
        return query.count()        