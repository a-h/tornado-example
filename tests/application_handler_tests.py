import json
from unittest import TestCase
from unittest.mock import MagicMock
from tornado import gen
from tornado.concurrent import Future
import app
from application_repository import ApplicationRepository

__author__ = 'adrian'

class ApplicationHandlerTests(TestCase):
    @gen.coroutine
    def test_that_applications_can_be_listed(self):
        # Arrange

        expected_data = {'some': 'data'}

        mock_application_repository = ApplicationRepository()
        future = Future()
        future.set_result(expected_data)
        mock_application_repository.list_applications = MagicMock(return_value=future)

        request = MagicMock()
        application = MagicMock()
        output = MagicMock()
        handler = app.ApplicationHandler(application, request, application_repository=mock_application_repository)
        handler.write = output

        # Act
        yield handler.get()

        # Assert
        output.assert_called_once_with(json.dumps(expected_data))
