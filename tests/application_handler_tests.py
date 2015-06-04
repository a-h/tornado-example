import json
from unittest import TestCase
from unittest.mock import MagicMock
import app
from application_repository import ApplicationRepository

__author__ = 'adrian'

class ApplicationHandlerTests(TestCase):
    def test_that_applications_can_be_listed(self):
        # Arrange
        mock_application_repository = ApplicationRepository()
        mock_application_repository.list_applications = MagicMock(return_value={'some': 'data'})

        request = MagicMock()
        application = MagicMock()
        output = MagicMock()
        handler = app.ApplicationHandler(application, request, application_repository=mock_application_repository)
        handler.write = output

        # Act
        handler.get()

        # Assert
        output.assert_called_once_with(json.dumps({'some': 'data'}))
