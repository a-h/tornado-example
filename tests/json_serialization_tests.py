from asyncio.test_utils import TestCase
import json
from unittest.mock import MagicMock, Mock
from schematics.exceptions import ModelValidationError
from tornado.test.web_test import WebTestCase
import app
from application_repository import ApplicationRepository
from models.application_model import ApplicationModel

__author__ = 'adrian'

import unittest


class ModelValidationTests(TestCase):
    def test_that_applications_must_have_a_name(self):
        app_model = ApplicationModel()

        with self.assertRaises(ModelValidationError):
            app_model.validate()


if __name__ == '__main__':
    unittest.main()
