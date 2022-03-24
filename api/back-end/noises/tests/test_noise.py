from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return 

class TestView(TestBase):
    def test_get_noise_cat(self, mock_func0):
        response = self.client.get(url_for('noise'), json={"animal":"cat"})
        self.assert200(response)
        self.assertIn(b'meow,', response.data)