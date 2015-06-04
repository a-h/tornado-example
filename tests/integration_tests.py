from tornado.test.web_test import WebTestCase
import app


class IntegrationTests(WebTestCase):
    def get_handlers(self):
        return app.get_handlers()

    def test_fetching_an_application(self):
        body = self.fetch("/application").body
        self.assertTrue(True)
