import unittest
from app import app, socketio
import os

class Test(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.socketio_client = socketio.test_client(app, flask_test_client=app.test_client())

    def test_home(self):
        assert self.app.get('/').status_code == 200

    def test_not_conn(self):
        print(self.socketio_client.is_connected())
        assert not self.socketio_client.is_connected()

unittest.main()