from asyncio.test_utils import TestCase
import json
from unittest.mock import MagicMock, Mock
from tornado.test.web_test import WebTestCase
import app
from application_repository import ApplicationRepository

__author__ = 'adrian'

import unittest


class UrlMatchingTests(TestCase):
    def find_handler(self, handlers, url):
        for handler in handlers:
            if handler.regex.match(url):
                return handler.handler_class
        return None

    def test_that_the_application_handler_handles_the_application_directory(self):
        handler = self.find_handler(app.get_handlers(), '/application/')
        self.assertEqual(handler, app.ApplicationHandler)


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


class IntegrationTests(WebTestCase):
    def get_handlers(self):
        return app.get_handlers()

    def test_fetching_an_application(self):
        body = self.fetch("/application").body
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
