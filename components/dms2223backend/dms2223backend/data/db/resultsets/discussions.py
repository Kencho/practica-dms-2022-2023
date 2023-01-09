""" Discussions class module.
"""

import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Discussion
from dms2223backend.data.db.exc import DiscussionExistsError


class Discussions():
    """ Class responsible of table-level discussions operations.
    """
    @staticmethod
    def create(session: Session, title: str, content: str) -> Discussion:
        """ Creates a new discussion record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - title (str): The title of the discussion string.
            - content (str): The content of the discussion string.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `Discussion` result.
        """
        if not title or not content:
            raise ValueError('A title and a content hash are required.')
        try:
            new_discussion = Discussion(title, content)
            session.add(new_discussion)
            session.commit()
            return new_discussion
        except IntegrityError as ex:
            raise DiscussionExistsError(
                'A discussion with name ' + title + ' already exists.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[Discussion]:
        """Lists every discussion.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Discussion]: A list of `Discussion` registers.
        """
        query = session.query(Discussion)
        return query.all()

    @staticmethod
    def get_discussion_by_id(session: Session, id: int,) -> Optional[Discussion]:
        """Obtains a discussion by an id.
        Args:
            - session (Session): The session object.
            - id (int): Id discussion integer.

        Returns:
            - Optional[Discussion]: The result of the `Discussion`.
        """

        if not id:
            raise ValueError('An id is requiered.')
        try:
            query = session.query(Discussion).filter_by(id=id)
            discussion: Discussion = query.one()
        except NoResultFound:
            return None
        return discussion
