from unittest import TestCase

from FTP_connection_test_case import FTP_connection_test_case

class Coonection_test_case(FTP_connection_test_case):
    def test_connection(self):
        actual_result = self._connection_status
        expected_result = '230'
        self.assertEqual(actual_result, expected_result, 'step 1')

if __name__ == '__main__':
    unittest.main()

