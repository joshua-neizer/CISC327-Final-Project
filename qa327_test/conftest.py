import pytest
import subprocess
import os
import signal
import time
import tempfile
from qa327.__main__ import app
from qa327.models import create_tables
import threading
from werkzeug.serving import make_server
from flask_sqlalchemy import SQLAlchemy

# separate port allows tests to be run while hosting
# actual app
FLASK_TEST_PORT = 8082

base_url = 'http://localhost:{}'.format(FLASK_TEST_PORT)

class ServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', FLASK_TEST_PORT, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


@pytest.fixture(scope="module", autouse=True)
def server():
    on_win = os.name == 'nt'
    with tempfile.TemporaryDirectory() as tmp_folder:
        # create a live server for testing
        # with a temporary file as database
        database_file = os.path.join(tmp_folder, 'db.sqlite')
        database_url = 'sqlite:///'+database_file
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        create_tables()

        server = ServerThread()
        server.start()
        time.sleep(5)
        yield
        server.shutdown()
        time.sleep(2)
        
