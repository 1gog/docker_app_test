from unittest import TestCase
from flask_webtest import TestApp
from main import app

class AppTestCase(TestCase):


    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        #flaskr.app.config['TESTING'] = True
        self.app = app
        self.app.config['SERVER_NAME'] = 'app:5000'

    def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(flaskr.app.config['DATABASE'])
        pass
   
    def test_root_app(self):
        self.app.get('/')
     

if __name__ == '__main__':
    unittest.main()

