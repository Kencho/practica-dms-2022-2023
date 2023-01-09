""" AnswerLogic class module.
"""

from typing import List
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db.results import Answer
from dms2223backend.data.db.resultsets import Answers, Comments

from dms2223backend.data.db.results import VoteAnswer



class AnswerLogic():
    """ Class with logic-level operations with the answers-related use cases.
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

        try:
            new_answer: Answer = Answers.answer(session, discussionid, content)
           
        except Exception as ex:
            raise ex
        return new_answer

    @staticmethod
    def list_all(session: Session) -> List[List]:
        """Lists every answer.

        Args:
            - session (Session): The session object.

        Returns:
            - List[List]: A list of `Discussion` registers.
        """
        return Answers.list_all(session)
        # answers = Answers.list_all(session)
        # list_of_answers : List[List] = []
        # for answer in answers:
        #     if (Comments.answer_has_comments(session, discussion.id)): #type: ignore
        #         list_of_answers.append([answer,1])
        #     else:
        #         list_of_answers.append([answer,0])
        # return list_of_answers
    
    @staticmethod
    def list_all_for_discussion(discussionid: int, session: Session) -> List[Answer]:
        """Lists the `answers made to a certain question.

        Args:
            - session (Session): The session object.
            - id (int): The question id.

        Raises:
            - ValueError: If the question id is missing.

        Returns:
            - List[Answer]: A list of answer registers with the question answers.
        """
        return Answers.list_all_for_discussion(session, discussionid)
    
    @staticmethod
    def get_answer(session: Session ,discussionid: int) -> Answer:
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Returns:
            - Answer: The Answer of the question.
        """
        try:
            answer: Answer = Answers.get_answer(session, discussionid)
        except Exception as ex:
            raise ex
        return answer

        # list_of_answers = []
        # try:
        #     answer: Answer = Answers.get_answer(session, discussionid)
        #     if (Comments.answer_has_comments(session, discussionid)):
        #         list_of_answers.append([answer, 1])
        #     else:
        #         list_of_answers.append([answer, 0])
        # except Exception as ex:
        #     raise ex
        # return list_of_answers
    
    @staticmethod
    def vote_answer(session: Session, aid: int ):
        """Vote an Answer

        Args:
            
            - aid: answer id.
            

        Returns:
            - Dict: Answer of the discussion.
        """
        
    

        try:
            vote: VoteAnswer = VoteAnswer(aid)
            session.add(vote)
            session.commit()
        except Exception as ex:
            raise ex
        return vote

    @staticmethod
    def get_vote(session: Session ,answerid: int) :
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Returns:
            - Answer: The Answer of the question.
        """
        try:
            vote: int = Answers.get_vote(session, answerid)
        except Exception as ex:
            raise ex
        return vote
    
    
        
        