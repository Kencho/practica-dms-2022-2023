""" ModeratorEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from dms2223frontend.data.rest.backendservice import BackendService
from .webauth import WebAuth
from .webquestion import WebQuestion
from .webanswer import WebAnswer
from .webcomment import WebComment


class ModeratorEndpoints():
    """ Monostate class responsible of handing the moderator web endpoint requests.
    """
    @staticmethod
    def get_moderator(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the moderator root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('moderator.html', name=name, roles=session['roles'])

    @staticmethod
    def get_moderator_reports(auth_service: AuthService,backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the reports root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']

        return render_template('moderator/reports.html', name=name, roles=session['roles'], reports=WebQuestion.list_reports(backend_service),
                                                                                            reportsanswer = WebQuestion.list_reports_answer(backend_service,),
                                                                                            reportscomment = WebQuestion.list_reports_comments(backend_service)
                                                                                            )

    @staticmethod
    def get_report_view(auth_service: AuthService,backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the report root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        id: int = int(str(request.args.get('reportid')))
        redirect_to = request.args.get('redirect_to', default='/moderator/reports')
        return render_template('moderator/moderator/view.html', name=name, roles=session['roles'], redirect_to=redirect_to,report = WebQuestion.get_report(backend_service,id))

    @staticmethod
    def put_accept_report(auth_service: AuthService,backend_service: BackendService) -> Union[Response, Text]:
        
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))

        id = request.form.get('idreport')

        new_discussion = WebQuestion.put_report(backend_service,
                                        id = id
                                        )
        if not new_discussion:
            return redirect(url_for('get_moderator'))
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_moderator_reports')

        return redirect(redirect_to)



    @staticmethod
    def get_moderator_discussions(auth_service: AuthService, backend_services: BackendService) -> Union[Response, Text]:
            """ Handles the GET requests to the reports root endpoint.
            Args:
                - auth_service (AuthService): The authentication service.
            Returns:
                - Union[Response,Text]: The generated response to the request.
            """
            if not WebAuth.test_token(auth_service):
                return redirect(url_for('get_login'))
            if Role.MODERATION.name not in session['roles']:
                return redirect(url_for('get_home'))
            name = session['user']
            return render_template('moderator/discussions.html', name=name, roles=session['roles'], discussions=WebQuestion.list_discussions(backend_services))

    # @staticmethod
    # def get_discussions_view(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
    #     """ Handles the GET requests to the discussion root endpoint.

    #     Args:
    #         - auth_service (AuthService): The authentication service.

    #     Returns:
    #         - Union[Response,Text]: The generated response to the request.
    #     """
    #     if not WebAuth.test_token(auth_service):
    #         return redirect(url_for('get_login'))
    #     if Role.DISCUSSION.name not in session['roles']:
    #         return redirect(url_for('get_home'))
    #     name = session['user']
    #     redirect_to = request.args.get('redirect_to', default='/moderator/discussions')
    #     id: int = int(str(request.args.get('discussionid')))
        
    #     return render_template('moderator/discussions/view.html', name=name, roles=session['roles'], redirect_to=redirect_to,
    #         discussion=WebQuestion.get_discussion(backend_service, id), answers = WebAnswer.list_answers(backend_service,id),
    #         comments = WebComment.list_comments(backend_service, id))

    @staticmethod
    def get_moderator_discussions_view(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        redirect_to = request.args.get('redirect_to', default='/moderator/discussions')
        id: int = int(str(request.args.get('discussionid')))
        
        return render_template('moderator/discussions/view.html', name=name, roles=session['roles'], redirect_to=redirect_to,
            discussion=WebQuestion.get_discussion(backend_service, id), answers = WebAnswer.list_answers(backend_service,id),
            comments = WebComment.list_comments(backend_service, id))

    @staticmethod
    def get_moderator_resolution_report(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the POST requests to the resolution report root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('reporttitle'))
        redirect_to = request.args.get('redirect_to', default='/moderator/moderator')
        return render_template('moderator/moderator/resolution.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title )


    @staticmethod
    def get_moderator_moderator_view(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('discussiontitle'))
        redirect_to = request.args.get('redirect_to', default='/moderator/reports')
        return render_template('moderator/moderator/view.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title)


