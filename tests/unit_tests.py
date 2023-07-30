import unittest
from app.influx import WrapperInfluxDB


class TestWrapperInfluxDB(unittest.TestCase):
    
    def setUp(self):
        self.db = WrapperInfluxDB()

    def test_query_method(self):
        query = 'SELECT * FROM my_table' #Use InfluxDB query language
        #Add in status code check
        result = self.db.query(query)
        expected_result = "..." # Replace this with the result you expect
        self.assertEqual(result, expected_result)

    def tearDown(self):
        # Assuming WrapperInfluxDB has a close method to close any connections
        self.db.close_connection()  
    

if __name__ == "__main__":
    unittest.main()
