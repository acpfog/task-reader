
import unittest 
from reader import app

class FlaskrTestCase(unittest.TestCase): 

    # Create a test client for the application
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    # End actions
    def tearDown(self):
        pass 

    # Send a GET request to the application and handle a response status code 
    def test_home_status_code(self):
        result = self.app.get('/stats') 
        self.assertEqual(result.status_code, 200) 

if __name__ == '__main__':
    unittest.main()

